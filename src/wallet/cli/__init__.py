import click
import orjson
import pkg_resources
import structlog
from config import load
from config.providers import EnvValueProvider

from wallet.app import AppConfig
from wallet.cli.accounts import accounts


structlog.configure(
    cache_logger_on_first_use=True,
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(serializer=orjson.dumps),
    ],
    logger_factory=structlog.BytesLoggerFactory(),
)


@click.group()
@click.option("--debug", is_flag=True, default=False)
@click.pass_context
def cli(ctx, debug: bool = False) -> None:
    config = AppConfig(defaults={"debug": debug})
    load(config, providers=[EnvValueProvider()])

    distribution = pkg_resources.get_distribution("wallet")

    ctx.obj["config"] = config
    ctx.obj["logger"] = structlog.get_logger(app_name=distribution.project_name, version=distribution.version)


def main() -> None:
    cli.add_command(accounts, name="accounts")

    cli(obj={})
