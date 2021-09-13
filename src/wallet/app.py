from config import BoolField, Config
from config.fields import NestedField, StrField


class WalletConfig(Config):
    host = StrField(env="WALLET_HOST", default="wallet.clayman.pro")
    token = StrField(env="WALLET_TOKEN")


class AppConfig(Config):
    debug = BoolField(default=False)
    wallet = NestedField[WalletConfig](WalletConfig, key="wallet")
