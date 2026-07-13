"""SSH driver for UniFi LED devices."""

from __future__ import annotations

import asyncio
import logging

import asyncssh

_LOGGER = logging.getLogger(__name__)


class UniFiLedDriver:
    """Low-level SSH driver."""

    def __init__(
        self,
        host: str,
        username: str,
        private_key: str,
        port: int = 22,
    ):

        self.host = host
        self.username = username
        self.private_key = private_key
        self.port = port

    async def _run(self, command: str):

        try:

            async with asyncssh.connect(

                host=self.host,

                username=self.username,

                client_keys=[self.private_key],

                known_hosts=None,

                port=self.port,

            ) as conn:

                result = await conn.run(command)

                return result.stdout.strip()

        except Exception as err:

            _LOGGER.error(err)

            return None

    async def turn_on(self):

        await self._run(

            "sed -i '/mgmt.led_pattern_override/d' "
            "/var/etc/persistent/cfg/mgmt && "
            "echo 'mgmt.led_pattern_override=1' >> "
            "/var/etc/persistent/cfg/mgmt && "
            "syswrapper.sh apply-config"

        )

    async def turn_off(self):

        await self._run(

            "sed -i '/mgmt.led_pattern_override/d' "
            "/var/etc/persistent/cfg/mgmt && "
            "echo 'mgmt.led_pattern_override=0' >> "
            "/var/etc/persistent/cfg/mgmt && "
            "syswrapper.sh apply-config"

        )

    async def set_rgb(
        self,
        r: int,
        g: int,
        b: int,
    ):

        command = (

            f'echo "{r},{g},{b}" > '

            "/proc/ubnt_ledbar/color"

        )

        await self._run(command)

    async def blue(self):

        await self.set_rgb(1, 23, 103)

    async def green(self):

        await self.set_rgb(0, 255, 0)

    async def red(self):

        await self.set_rgb(255, 0, 0)

    async def white(self):

        await self.set_rgb(255, 255, 255)
