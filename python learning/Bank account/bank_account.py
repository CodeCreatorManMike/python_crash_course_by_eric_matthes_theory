# project: Bank Account

# import statements:
import json
import os
from decimal import Decimal, ROUND_HALF_UP  # Decimal gives safe money math; ROUND_HALF_UP is typical bank rounding

DATA_FILE = "bank_users.json"  # the JSON file where we persist user data between runs


# default values for a brand new account (used to ensure the JSON schema is complete)
# NOTE: We store money values as strings in JSON (e.g. "0.00") and convert to Decimal in Python.
DEFAULTS = {
    "account_status": True,
    "current_account_balance": "0.00",
    "savings_account_balance": "0.00",
    "account_currency": "GBP",
    "overdraft_limit": "1000.00",
    "overdraft_used": "0.00",        # how much overdraft is currently consumed (only fees can increase this)
    "transfer_count": 0,
    "deposit_count": 0,
}

# helper to normalize any numeric/string input to Decimal with 2dp (bank-style)
def as_money(x) -> Decimal:
    """
    Convert x (str/int/float/Decimal) to Decimal with 2 decimal places.
    Using Decimal avoids float rounding errors (critical for money).
    """
    return Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


# initial module-level variables from your original code
account_status = False
current_account_balance = 0
savings_account_balance = 0
account_currency = 'GBP'
overdraft_limit = 1000
transfer_occurance = 0
deposit_occurance = 0

user_email = []
user_password = []


class Account:
    """Overall class to manage user auth, balances, transfers, and persistence (JSON)."""

    def __init__(self):
        # expose helpers (your original idea) — now bound to instance methods
        self.load_data = self._load_data    # fixed: must reference instance method
        self.save_data = self._save_data    # fixed: must reference instance method

        # user identity & runtime state (start empty until login)
        self.user_email = None
        self.user_password = None

        # account attributes (set to safe defaults; replaced on login)
        self.account_status = False
        self.account_currency = "GBP"
        self.current_account_balance = as_money("0.00")
        self.savings_account_balance = as_money("0.00")
        self.overdraft_limit = as_money("1000.00")

        # overdraft_used tracks how much of the overdraft limit is consumed.
        # IMPORTANT: per your rule, ONLY fees can push this up; principals (withdraw/transfer) cannot.
        self.overdraft_used = as_money("0.00")

        # counters (educational: these show how to track usage across runs)
        self.transfer_count = 0
        self.deposit_count = 0

        # scratch values from recent operations (used by fee/interest previews etc.)
        self.deposit_amount = as_money("0.00")
        self.withdrawal_amount = as_money("0.00")
        self.transfer_amount = as_money("0.00")
        self.transfer_type = None  # 'A' (to savings) or 'B' (payment)

    # JSON storage
    def _load_data(self):
        """
        load existing data or create empty structure.

        JSON -> Python dict:
        - We read the entire file once per operation.
        - If the file doesn't exist yet, we return {} so the program can create it.
        """
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                data = json.load(file)  # loads the JSON file contents into a Python dictionary
        else:
            data = {}  # create an empty dictionary if file doesn’t exist
        return data
    
    def _save_data(self, data: dict) -> None:
        """
        safely write JSON to disk (atomic replace).

        We write to a temporary file first, then replace the original.
        This avoids partial writes if the program crashes mid-write.
        """
        tmp = DATA_FILE + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)  # dumps (writes) the dictionary back into JSON format
        os.replace(tmp, DATA_FILE)  # replaces old file with the new one safely

    def _ensure_user_record(self, data: dict, email: str) -> None:
        """
        Educational: JSON schema guard.
        Ensures the user's JSON record has ALL fields we expect.
        This is useful if the schema evolves over time.
        """
        if email not in data:
            raise KeyError("User record missing unexpectedly.")
        rec = data[email]
        for k, v in DEFAULTS.items():
            if k not in rec:
                rec[k] = v

    # setup
    def login_in(self):
        """
        Log in or create a new account if it doesn't exist.
        - Reads JSON, checks if the user exists.
        - If exists, verifies password and loads their balances.
        - If not, creates a new record with DEFAULTS and persists it.
        """
        self.user_email = input("Email: ").strip().lower()
        self.user_password = input("Password: ").strip()

        data = self._load_data()  # loads JSON data so we can check if user exists

        email = self.user_email
        password = self.user_password

        if email in data:
            # existing user: verify password
            if data[email]['password'] != password:
                print('\nIncorrect password.')
                return False

            # schema fix-up (if older records were missing fields)
            self._ensure_user_record(data, email)
            self._save_data(data)  # persist any schema fixes

            print(f"\nWelcome back, {email}!")
            self._load_user_into_state(email, data[email])
            return True
        else:
            # new user: create with defaults
            data[email] = {
                "password": password,
                **DEFAULTS,   # copy in our complete set of default fields
            }

            self._save_data(data)  # saves the new user’s info back to the JSON file
            print(f"\nAccount created. Welcome, {email}!")
            self._load_user_into_state(email, data[email])
            return True
    
    def _load_user_into_state(self, email: str, record: dict) -> None:
        """
        Copy JSON record into this instance’s attributes.

        NOTE on money:
        - JSON stores money as strings (e.g., "12.34")
        - We convert to Decimal here for precise arithmetic during runtime.
        """
        self.user_email = email
        self.user_password = record["password"]               # (not recommended to keep in RAM in real apps)
        self.account_status = bool(record.get("account_status", True))
        self.account_currency = record.get("account_currency", "GBP")
        # Convert persisted strings to Decimal
        self.current_account_balance = as_money(record.get("current_account_balance", "0.00"))
        self.savings_account_balance = as_money(record.get("savings_account_balance", "0.00"))
        self.overdraft_limit = as_money(record.get("overdraft_limit", "1000.00"))
        self.overdraft_used = as_money(record.get("overdraft_used", "0.00"))
        self.transfer_count = int(record.get("transfer_count", 0))
        self.deposit_count = int(record.get("deposit_count", 0))

    # ---------- internal helpers for fees/interest/overdraft (educational section) ----------

    def _overdraft_remaining(self) -> Decimal:
        """
        How much overdraft is still available (limit - used).
        This prevents fees from exceeding the overdraft cap.
        """
        return (self.overdraft_limit - self.overdraft_used).quantize(Decimal("0.01"))

    def _apply_fee(self, base_amount: Decimal, kind: str) -> Decimal:
        """
        Calculate and apply a fee.

        IMPORTANT RULE (your requirement):
        - Only fees are allowed to use overdraft.
        - If the current balance can't cover the fee, we dip into overdraft_used.
        - Principal for deposits/withdrawals/transfers NEVER touches overdraft.

        kind: one of {"deposit", "withdrawal", "transfer_savings", "payment"}.
        Returns the fee charged (Decimal).
        """
        # simple fee rate table (educational — tweak to your needs)
        rates = {
            "deposit": Decimal("0.05"),            # 5%
            "withdrawal": Decimal("0.11"),         # 11%
            "transfer_savings": Decimal("0.01"),   # 1%
            "payment": Decimal("0.08"),            # 8%
        }
        rate = rates.get(kind, Decimal("0.00"))
        fee = (base_amount * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        if fee <= 0:
            return as_money("0.00")

        # First attempt: pay fee from current balance
        if self.current_account_balance >= fee:
            self.current_account_balance -= fee
            return fee

        # Not enough current balance → use overdraft for the shortfall
        shortfall = fee - self.current_account_balance

        # Zero the current balance (fee consumes it)
        self.current_account_balance = as_money("0.00")

        # Check overdraft availability
        if shortfall > self._overdraft_remaining():
            # Educational note:
            # In stricter systems, you'd abort the *entire* operation BEFORE applying a fee
            # if you know the fee cannot be covered. Here, we raise an error to signal failure.
            print("\nFee cannot be charged: overdraft limit would be exceeded.")
            raise ValueError("Insufficient overdraft to cover fee.")

        # consume overdraft for the shortfall
        self.overdraft_used += shortfall
        return fee

    def _forecast_interest_amount(self, principal: Decimal, rate_decimal: Decimal, years: int) -> Decimal:
        """
        Purely computational (no side effects): A = P * (1 + r)^t
        rate_decimal is e.g. Decimal('0.03') for 3% per year.
        """
        return (principal * (Decimal("1.0") + rate_decimal) ** years).quantize(Decimal("0.01"))

    # main loop
    def deposit(self):
        """
        Deposit flow:
        - Read JSON (data snapshot)
        - Validate amount
        - Increase current balance by the deposit amount
        - Optionally apply a fee (fee may use overdraft if needed)
        - Persist back to JSON

        EDUCATIONAL: We use Decimal for all arithmetic, then write as strings to JSON.
        """
        data = self._load_data()  # loads the JSON file contents into a dictionary in memory
        self._ensure_user_record(data, self.user_email)

        # getting users desired deposit amount
        try:
            deposit_amount = as_money(input('\nHow much would you like to deposit today? '))
        except Exception:
            print("\nInvalid amount.")
            return

        if deposit_amount <= 0:
            print("\nAmount must be greater than 0.")
            return

        self.deposit_amount = deposit_amount
        print(f"\n{deposit_amount} GBP depositing...")

        # adding the current account balance and the new deposit
        self.current_account_balance += deposit_amount
        self.deposit_count += 1

        # Apply a deposit fee (if you want fee-less deposits, comment this out)
        self._apply_fee(deposit_amount, "deposit")

        # saving the new information back to the json file
        rec = data[self.user_email]
        rec["current_account_balance"] = str(self.current_account_balance)
        rec["overdraft_used"] = str(self.overdraft_used)
        rec["deposit_count"] = self.deposit_count
        self._save_data(data)  # writes (updates) the modified dictionary back into the file

        print(f"\nDeposit completed. Current balance: £{self.current_account_balance:.2f}")

    def withdrawal(self):
        """
        Withdrawal flow:
        - Read JSON
        - Validate amount
        - Ensure sufficient funds (withdrawals cannot use overdraft for the principal)
        - Subtract from current balance
        - Optionally apply a withdrawal fee (fee MAY use overdraft)
        - Persist
        """
        data = self._load_data()
        self._ensure_user_record(data, self.user_email)

        # loading in the current account balance to use (already in self.* as Decimal)
        try:
            withdrawal_amount = as_money(input("\nHow much would you like to withdraw today? "))
        except Exception:
            print("\nInvalid amount.")
            return

        if withdrawal_amount <= 0:
            print("\nAmount must be greater than 0.")
            return

        print(f"\n{withdrawal_amount} GBP withdrawing...")

        # Regular withdrawals CANNOT use overdraft (principal rule)
        if self.current_account_balance < withdrawal_amount:
            print("\nInsufficient funds (withdrawals cannot use overdraft).")
            return

        # removing the withdrawal amount from the current balance
        self.current_account_balance -= withdrawal_amount
        self.withdrawal_amount = withdrawal_amount

        # Apply a withdrawal fee (fee MAY use overdraft if needed)
        self._apply_fee(withdrawal_amount, "withdrawal")

        # saving the new information back to the json file
        rec = data[self.user_email]
        rec["current_account_balance"] = str(self.current_account_balance)
        rec["overdraft_used"] = str(self.overdraft_used)
        self._save_data(data)

        print("\nWithdrawal completed.")
        print(f"Current balance: £{self.current_account_balance:.2f}")

    def transfer(self):
        """
        Transfer flow:
        - Two types:
          A) Savings Account Transfer (move from current -> savings)
          B) Payment Transfer (send to another user's current account)
        - Principal NEVER uses overdraft (per your rule)
        - Fee MAY use overdraft (applied after principal move)
        - Persist all updates to JSON
        """
        data = self._load_data()  # JSON -> Python dict in memory
        self._ensure_user_record(data, self.user_email)

        print("\nWhat transfer type would you like to make? ")
        transfer_type = input("\nA: Savings Account Transfer  B: Payment Transfer ").strip().upper()
        self.transfer_type = transfer_type  # remember what type we did for fee explanation etc.

        if transfer_type not in ("A", "B"):
            print("\nInvalid Input.")
            return

        try:
            transfer_amount = as_money(input("\nHow much would you like to transfer today? "))
        except Exception:
            print("\nInvalid amount.")
            return

        if transfer_amount <= 0:
            print("\nAmount must be greater than 0.")
            return

        self.transfer_amount = transfer_amount

        if transfer_type == 'A':
            # Savings Account Transfer (current -> savings).
            # Principal CANNOT use overdraft.
            if self.current_account_balance < transfer_amount:
                print("\nYou do not have enough funds to make this transfer (no overdraft for principal).")
                return

            print("\nTransfer in progress...")
            # adding transfer amount to savings account
            self.savings_account_balance += transfer_amount
            # updating current account balance
            self.current_account_balance -= transfer_amount

            # Apply fee for savings transfer (fee MAY dip into overdraft)
            self._apply_fee(transfer_amount, "transfer_savings")

            # persist sender's balances
            rec = data[self.user_email]
            rec["current_account_balance"] = str(self.current_account_balance)
            rec["savings_account_balance"] = str(self.savings_account_balance)
            rec["overdraft_used"] = str(self.overdraft_used)

            # counter (educational: track how many transfers)
            self.transfer_count += 1
            rec["transfer_count"] = self.transfer_count

            self._save_data(data)

            print("\nTransfer completed.")
            print(f"Current: £{self.current_account_balance:.2f} | Savings: £{self.savings_account_balance:.2f}")

        elif transfer_type == 'B':
            # Payment Transfer (current -> another user's current).
            # Principal CANNOT use overdraft.
            if self.current_account_balance < transfer_amount:
                print("\nYou do not have enough funds to make this transfer (no overdraft for principal).")
                return

            recipient = input("\nWho are you sending the money to? (email) ").strip().lower()
            if recipient == self.user_email:
                print("\nCannot send a payment to yourself.")
                return
            if recipient not in data:
                print("\nRecipient not found.")
                return

            # Ensure recipient schema is complete (educational: schema migration safety)
            self._ensure_user_record(data, recipient)

            print("\nTransfer in progress...")

            # move principal: sender -> recipient (no overdraft)
            self.current_account_balance -= transfer_amount
            recipients_current_balance = as_money(data[recipient]["current_account_balance"])
            recipients_current_balance += transfer_amount
            data[recipient]["current_account_balance"] = str(recipients_current_balance)

            # Apply payment fee (fee MAY dip into overdraft)
            self._apply_fee(transfer_amount, "payment")

            # persist sender and recipient
            srec = data[self.user_email]
            srec["current_account_balance"] = str(self.current_account_balance)
            srec["overdraft_used"] = str(self.overdraft_used)
            self.transfer_count += 1
            srec["transfer_count"] = self.transfer_count

            self._save_data(data)

            print("\nTransfer completed.")
            print(f"Your current balance: £{self.current_account_balance:.2f}")

    # ---------- NEW: account summary (what the user sees at a glance) ----------
    def account_summary(self):
        """
        Show a concise summary of the account.

        We read from JSON to make sure we're showing the most up-to-date persisted values,
        then display current balance, savings balance, currency, and overdraft status.
        """
        data = self._load_data()                 # JSON -> dict (latest snapshot from disk)
        self._ensure_user_record(data, self.user_email)

        rec = data[self.user_email]              # the user's stored record

        # Convert JSON strings to Decimal for formatting/consistency
        current = as_money(rec["current_account_balance"])
        savings = as_money(rec["savings_account_balance"])
        currency = rec.get("account_currency", "GBP")
        od_limit = as_money(rec.get("overdraft_limit", "0.00"))
        od_used = as_money(rec.get("overdraft_used", "0.00"))
        od_remaining = (od_limit - od_used).quantize(Decimal("0.01"))

        # Optional: totals to help users reason about their money at a glance
        total_holdings = (current + savings).quantize(Decimal("0.01"))

        print("\n=== Account Summary ===")
        print(f"User: {self.user_email}")
        print(f"Currency: {currency}")
        print(f"Current balance: £{current:.2f}")
        print(f"Savings balance: £{savings:.2f}")
        print(f"Total (current + savings): £{total_holdings:.2f}")
        print(f"Overdraft used: £{od_used:.2f} / £{od_limit:.2f} (remaining £{od_remaining:.2f})")
        print(f"Deposits made: {int(rec.get('deposit_count', 0))} | Transfers made: {int(rec.get('transfer_count', 0))}")
        print("========================")

    # ---------- Extra educational utilities (optional to call) ----------

    def fee_breakdown_preview(self, amount: Decimal, kind: str):
        """
        Educational: Preview how fees are computed for a given kind without changing balances.
        This helps you 'see' the rule table.
        """
        rates = {
            "deposit": Decimal("0.05"),
            "withdrawal": Decimal("0.11"),
            "transfer_savings": Decimal("0.01"),
            "payment": Decimal("0.08"),
        }
        rate = rates.get(kind, Decimal("0.00"))
        fee = (as_money(amount) * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        print(f"Kind={kind} Amount=£{as_money(amount):.2f} Fee=£{fee:.2f}")

    def interest_forecast(self):
        """
        Educational: show what your current savings could become at an annual rate (compounded).
        This is a forecast (no changes are persisted).
        """
        try:
            rate_pct = as_money(input("\nEnter annual interest rate as % (e.g., 3 for 3%): "))
        except Exception:
            print("\nInvalid rate.")
            return

        rate = rate_pct / Decimal("100")  # convert percent to decimal
        years = [3, 5, 10]
        principal = self.savings_account_balance

        print(f"\nForecast for savings of £{principal:.2f} at {rate_pct:.2f}% per year (compounded):")
        for t in years:
            total = self._forecast_interest_amount(principal, rate, t)
            print(f"  {t} years: £{total:.2f}")
