# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "notification-hub",
    is_experimental=True,
)
class __CMDGroup(AAZCommandGroup):
    """Manage notification hubs.
    """
    pass


__all__ = ["__CMDGroup"]
