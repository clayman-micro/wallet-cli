from logging import Logger

import click
from rich.console import Console
from rich.table import Table

from wallet.cli.base import coro
from wallet.core.services.accounts import AccountService
from wallet.gateways.accounts import AccountHTTPGateway


@click.group()
@click.pass_context
@coro
async def accounts(ctx: click.Context) -> None:
    logger: Logger = ctx.obj["logger"]
    logger.debug("Accounts")


@accounts.command()
@click.pass_context
@coro
async def add(ctx: click.Context) -> None:
    """Add new account."""

    logger: Logger = ctx.obj["logger"]
    logger.debug("Add new account")


@accounts.command()
@click.pass_context
@coro
async def show(ctx: click.Context) -> None:
    """Show all accounts."""

    config = ctx.obj["config"]

    service = AccountService(gateway=AccountHTTPGateway(host=config.wallet.host, token=config.wallet.token))
    accounts = await service.get_accounts()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=12)
    table.add_column("Name")

    for account in accounts:
        table.add_row(str(account.key), account.name)

    console = Console()
    console.print(table)
