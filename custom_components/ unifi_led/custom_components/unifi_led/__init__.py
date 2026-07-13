from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import UniFiLedCoordinator


async def async_setup(hass, config):

    hass.data.setdefault(DOMAIN, {})

    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry
):

    coordinator = UniFiLedCoordinator(
        hass,
        entry
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(
        entry,
        ["button", "sensor"]
    )

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: ConfigEntry
):

    unload_ok = await hass.config_entries.async_unload_platforms(
        entry,
        ["button", "sensor"]
    )

    if unload_ok:

        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
