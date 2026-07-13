# Home Assistant UniFi LED Control

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026+-41BDF5.svg)
![UniFi](https://img.shields.io/badge/UniFi-E7-0559C9.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-success.svg)

Control the status LED of UniFi Access Points directly from Home Assistant using SSH.

Originally developed for the **UniFi E7**, this project provides an easy way to integrate the AP LED into Home Assistant automations, allowing it to become a visual notification device for network status, alarms, presence detection, and any custom automation.

---

## Features

✔ Turn LED ON/OFF

✔ Change LED color

✔ Full Home Assistant integration

✔ Ready-to-use shell commands

✔ Template entities

✔ Example automations

✔ Mushroom Dashboard

✔ Blueprint (coming soon)

✔ Extensive documentation

---

## Supported Hardware

Currently tested on:

| Device | Status |
|---------|--------|
| UniFi E7 | ✅ Fully Supported |

Other UniFi devices using the same LED configuration mechanism may also work.

Community feedback is welcome.

---

## Example Uses

Internet Status

🔵 Both WANs Online

🟢 WAN Failover

🔴 Internet Offline

---

Alarm

🟢 Disarmed

🟡 Armed

🔴 Triggered

---

Presence

🔵 Home

⚪ Away

🟣 Night

---

Home Modes

Movie Mode

Vacation

Guest Mode

Maintenance

---

## How it Works

Home Assistant

↓

SSH

↓

UniFi Access Point

↓

Persistent configuration

↓

LED changes instantly

No custom firmware.

No modifications.

No unsupported software.

Only SSH access.

---

## Installation

1. Enable SSH authentication.

2. Copy the package.

3. Copy shell_commands.yaml

4. Restart Home Assistant.

5. Import the Blueprint (optional).

Done.

---

## Limitations

Current known limitations:

• LED brightness cannot be adjusted.

The firmware parameter that initially appeared to control brightness only enables or disables the LED.

Intermediate brightness levels are not supported.

• Animations are not currently supported.

• Fade effects are not available.

---

## Roadmap

Version 1.0

- LED color control

- Home Assistant package

- Dashboard

- Documentation

Version 1.1

- Blueprint

- Multi-device support

- Installation wizard

Version 2.0

- Automatic AP discovery

- Device selector

- Native Integration (research)

---

## Repository Structure

```

ha-unifi-led-control/

README.md

LICENSE

packages/

shell_commands.yaml

scripts.yaml

automations.yaml

blueprints/

dashboard/

examples/

docs/

images/

```

---

## Documentation

Installation Guide

Configuration Guide

Troubleshooting

Reverse Engineering

FAQ

Examples

---

## Why This Project?

The UniFi LED is usually ignored.

Instead of displaying only the factory status, it can become a fully programmable visual indicator integrated with Home Assistant.

This project transforms the Access Point into a smart notification device.

---

## Disclaimer

This project is not affiliated with Ubiquiti Inc.

Use at your own risk.

Always keep backups of your device configuration before making changes.

---

## Contributing

Contributions are welcome.

Issues

Pull Requests

Ideas

Bug Reports

Documentation Improvements

---

## License

MIT License
