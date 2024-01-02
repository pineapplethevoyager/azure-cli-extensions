# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "palo-alto cloudngfw firewall show",
)
class Show(AAZCommand):
    """Get a FirewallResource

    :example: Get a FirewallResource
        az palo-alto cloudngfw firewall show --name MyCloudngfwFirewall -g MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-08-29",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/paloaltonetworks.cloudngfw/firewalls/{}", "2022-08-29"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.firewall_name = AAZStrArg(
            options=["-n", "--name", "--firewall-name"],
            help="Firewall resource name",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FirewallsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FirewallsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/firewalls/{firewallName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "firewallName", self.ctx.args.firewall_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-29",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
            )

            properties = cls._schema_on_200.properties
            properties.associated_rulestack = AAZObjectType(
                serialized_name="associatedRulestack",
            )
            properties.dns_settings = AAZObjectType(
                serialized_name="dnsSettings",
                flags={"required": True},
            )
            properties.front_end_settings = AAZListType(
                serialized_name="frontEndSettings",
            )
            properties.is_panorama_managed = AAZStrType(
                serialized_name="isPanoramaManaged",
            )
            properties.marketplace_details = AAZObjectType(
                serialized_name="marketplaceDetails",
                flags={"required": True},
            )
            properties.network_profile = AAZObjectType(
                serialized_name="networkProfile",
                flags={"required": True},
            )
            properties.pan_etag = AAZStrType(
                serialized_name="panEtag",
            )
            properties.panorama_config = AAZObjectType(
                serialized_name="panoramaConfig",
            )
            properties.plan_data = AAZObjectType(
                serialized_name="planData",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            associated_rulestack = cls._schema_on_200.properties.associated_rulestack
            associated_rulestack.location = AAZStrType()
            associated_rulestack.resource_id = AAZStrType(
                serialized_name="resourceId",
            )
            associated_rulestack.rulestack_id = AAZStrType(
                serialized_name="rulestackId",
            )

            dns_settings = cls._schema_on_200.properties.dns_settings
            dns_settings.dns_servers = AAZListType(
                serialized_name="dnsServers",
            )
            dns_settings.enable_dns_proxy = AAZStrType(
                serialized_name="enableDnsProxy",
            )
            dns_settings.enabled_dns_type = AAZStrType(
                serialized_name="enabledDnsType",
            )

            dns_servers = cls._schema_on_200.properties.dns_settings.dns_servers
            dns_servers.Element = AAZObjectType()
            _ShowHelper._build_schema_ip_address_read(dns_servers.Element)

            front_end_settings = cls._schema_on_200.properties.front_end_settings
            front_end_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.front_end_settings.Element
            _element.backend_configuration = AAZObjectType(
                serialized_name="backendConfiguration",
                flags={"required": True},
            )
            _ShowHelper._build_schema_endpoint_configuration_read(_element.backend_configuration)
            _element.frontend_configuration = AAZObjectType(
                serialized_name="frontendConfiguration",
                flags={"required": True},
            )
            _ShowHelper._build_schema_endpoint_configuration_read(_element.frontend_configuration)
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.protocol = AAZStrType(
                flags={"required": True},
            )

            marketplace_details = cls._schema_on_200.properties.marketplace_details
            marketplace_details.marketplace_subscription_id = AAZStrType(
                serialized_name="marketplaceSubscriptionId",
                flags={"read_only": True},
            )
            marketplace_details.marketplace_subscription_status = AAZStrType(
                serialized_name="marketplaceSubscriptionStatus",
            )
            marketplace_details.offer_id = AAZStrType(
                serialized_name="offerId",
                flags={"required": True},
            )
            marketplace_details.publisher_id = AAZStrType(
                serialized_name="publisherId",
                flags={"required": True},
            )

            network_profile = cls._schema_on_200.properties.network_profile
            network_profile.egress_nat_ip = AAZListType(
                serialized_name="egressNatIp",
            )
            network_profile.enable_egress_nat = AAZStrType(
                serialized_name="enableEgressNat",
                flags={"required": True},
            )
            network_profile.network_type = AAZStrType(
                serialized_name="networkType",
                flags={"required": True},
            )
            network_profile.public_ips = AAZListType(
                serialized_name="publicIps",
                flags={"required": True},
            )
            network_profile.vnet_configuration = AAZObjectType(
                serialized_name="vnetConfiguration",
            )
            network_profile.vwan_configuration = AAZObjectType(
                serialized_name="vwanConfiguration",
            )

            egress_nat_ip = cls._schema_on_200.properties.network_profile.egress_nat_ip
            egress_nat_ip.Element = AAZObjectType()
            _ShowHelper._build_schema_ip_address_read(egress_nat_ip.Element)

            public_ips = cls._schema_on_200.properties.network_profile.public_ips
            public_ips.Element = AAZObjectType()
            _ShowHelper._build_schema_ip_address_read(public_ips.Element)

            vnet_configuration = cls._schema_on_200.properties.network_profile.vnet_configuration
            vnet_configuration.ip_of_trust_subnet_for_udr = AAZObjectType(
                serialized_name="ipOfTrustSubnetForUdr",
            )
            _ShowHelper._build_schema_ip_address_read(vnet_configuration.ip_of_trust_subnet_for_udr)
            vnet_configuration.trust_subnet = AAZObjectType(
                serialized_name="trustSubnet",
                flags={"required": True},
            )
            _ShowHelper._build_schema_ip_address_space_read(vnet_configuration.trust_subnet)
            vnet_configuration.un_trust_subnet = AAZObjectType(
                serialized_name="unTrustSubnet",
                flags={"required": True},
            )
            _ShowHelper._build_schema_ip_address_space_read(vnet_configuration.un_trust_subnet)
            vnet_configuration.vnet = AAZObjectType(
                flags={"required": True},
            )
            _ShowHelper._build_schema_ip_address_space_read(vnet_configuration.vnet)

            vwan_configuration = cls._schema_on_200.properties.network_profile.vwan_configuration
            vwan_configuration.ip_of_trust_subnet_for_udr = AAZObjectType(
                serialized_name="ipOfTrustSubnetForUdr",
            )
            _ShowHelper._build_schema_ip_address_read(vwan_configuration.ip_of_trust_subnet_for_udr)
            vwan_configuration.network_virtual_appliance_id = AAZStrType(
                serialized_name="networkVirtualApplianceId",
            )
            vwan_configuration.trust_subnet = AAZObjectType(
                serialized_name="trustSubnet",
            )
            _ShowHelper._build_schema_ip_address_space_read(vwan_configuration.trust_subnet)
            vwan_configuration.un_trust_subnet = AAZObjectType(
                serialized_name="unTrustSubnet",
            )
            _ShowHelper._build_schema_ip_address_space_read(vwan_configuration.un_trust_subnet)
            vwan_configuration.v_hub = AAZObjectType(
                serialized_name="vHub",
                flags={"required": True},
            )
            _ShowHelper._build_schema_ip_address_space_read(vwan_configuration.v_hub)

            panorama_config = cls._schema_on_200.properties.panorama_config
            panorama_config.cg_name = AAZStrType(
                serialized_name="cgName",
                flags={"read_only": True},
            )
            panorama_config.config_string = AAZStrType(
                serialized_name="configString",
                flags={"required": True},
            )
            panorama_config.dg_name = AAZStrType(
                serialized_name="dgName",
                flags={"read_only": True},
            )
            panorama_config.host_name = AAZStrType(
                serialized_name="hostName",
                flags={"read_only": True},
            )
            panorama_config.panorama_server = AAZStrType(
                serialized_name="panoramaServer",
                flags={"read_only": True},
            )
            panorama_config.panorama_server2 = AAZStrType(
                serialized_name="panoramaServer2",
                flags={"read_only": True},
            )
            panorama_config.tpl_name = AAZStrType(
                serialized_name="tplName",
                flags={"read_only": True},
            )
            panorama_config.vm_auth_key = AAZStrType(
                serialized_name="vmAuthKey",
                flags={"read_only": True},
            )

            plan_data = cls._schema_on_200.properties.plan_data
            plan_data.billing_cycle = AAZStrType(
                serialized_name="billingCycle",
                flags={"required": True},
            )
            plan_data.effective_date = AAZStrType(
                serialized_name="effectiveDate",
                flags={"read_only": True},
            )
            plan_data.plan_id = AAZStrType(
                serialized_name="planId",
                flags={"required": True},
            )
            plan_data.usage_type = AAZStrType(
                serialized_name="usageType",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_endpoint_configuration_read = None

    @classmethod
    def _build_schema_endpoint_configuration_read(cls, _schema):
        if cls._schema_endpoint_configuration_read is not None:
            _schema.address = cls._schema_endpoint_configuration_read.address
            _schema.port = cls._schema_endpoint_configuration_read.port
            return

        cls._schema_endpoint_configuration_read = _schema_endpoint_configuration_read = AAZObjectType()

        endpoint_configuration_read = _schema_endpoint_configuration_read
        endpoint_configuration_read.address = AAZObjectType(
            flags={"required": True},
        )
        cls._build_schema_ip_address_read(endpoint_configuration_read.address)
        endpoint_configuration_read.port = AAZStrType(
            flags={"required": True},
        )

        _schema.address = cls._schema_endpoint_configuration_read.address
        _schema.port = cls._schema_endpoint_configuration_read.port

    _schema_ip_address_space_read = None

    @classmethod
    def _build_schema_ip_address_space_read(cls, _schema):
        if cls._schema_ip_address_space_read is not None:
            _schema.address_space = cls._schema_ip_address_space_read.address_space
            _schema.resource_id = cls._schema_ip_address_space_read.resource_id
            return

        cls._schema_ip_address_space_read = _schema_ip_address_space_read = AAZObjectType()

        ip_address_space_read = _schema_ip_address_space_read
        ip_address_space_read.address_space = AAZStrType(
            serialized_name="addressSpace",
        )
        ip_address_space_read.resource_id = AAZStrType(
            serialized_name="resourceId",
        )

        _schema.address_space = cls._schema_ip_address_space_read.address_space
        _schema.resource_id = cls._schema_ip_address_space_read.resource_id

    _schema_ip_address_read = None

    @classmethod
    def _build_schema_ip_address_read(cls, _schema):
        if cls._schema_ip_address_read is not None:
            _schema.address = cls._schema_ip_address_read.address
            _schema.resource_id = cls._schema_ip_address_read.resource_id
            return

        cls._schema_ip_address_read = _schema_ip_address_read = AAZObjectType()

        ip_address_read = _schema_ip_address_read
        ip_address_read.address = AAZStrType()
        ip_address_read.resource_id = AAZStrType(
            serialized_name="resourceId",
        )

        _schema.address = cls._schema_ip_address_read.address
        _schema.resource_id = cls._schema_ip_address_read.resource_id


__all__ = ["Show"]
