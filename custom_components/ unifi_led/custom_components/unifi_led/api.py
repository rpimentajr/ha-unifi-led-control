"""UniFi LED SSH API."""

from __future__ import annotations

import logging

import asyncssh

from .const import (
    COLOR_MAP,
)

_LOGGER = logging.getLogger(__name__)


class UniFiLedAPI:
    """Control UniFi LED through SSH."""

    def __init__(
        self,
        host: str,
        username: str,
        private_key: str,
    ) -> None:

        self.host = host
        self.username = username
        self.private_key = private_key


    async def _execute(
        self,
        command: str,
    ) -> str | None:
        """Execute SSH command."""

        try:

            async with asyncssh.connect(

                self.host,

                username=self.username,

                client_keys=[self.private_key],

                known_hosts=None,

            ) as connection:

                result = await connection.run(
                    command,
                    check=True
                )

                return result.stdout


        except Exception as error:

            _LOGGER.error(
                "UniFi LED SSH error: %s",
                error
            )

            return None


    async def set_enabled(
        self,
        enabled: bool,
    ) -> None:
        """Enable or disable LED."""

        value = 1 if enabled else 0

        command = (

            "sed -i '/mgmt.led_pattern_override/d' "
            "/var/etc/persistent/cfg/mgmt && "

            f"echo 'mgmt.led_pattern_override={value}' "
            ">> /var/etc/persistent/cfg/mgmt && "

            "syswrapper.sh apply-config"

        )

        await self._execute(command)


    async def set_rgb(
        self,
        rgb: str,
    ) -> None:
        """Set LED RGB color."""

        command = (

            f'echo "{rgb}" '

            "> /proc/ubnt_ledbar/color"

        )

        await self._execute(command)


    async def set_color(
        self,
        color: str,
    ) -> None:
        """Set LED named color."""

        rgb = COLOR_MAP.get(color.lower())

        if rgb is None:

            raise ValueError(
                f"Unsupported color: {color}"
            )

        await self.set_enabled(True)

        await self.set_rgb(rgb)
