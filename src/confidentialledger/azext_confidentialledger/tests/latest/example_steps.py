# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .. import try_manual


# EXAMPLE: /Ledger/put/ConfidentialLedgerCreate
@try_manual
def step_create(test, checks=None):
    if checks is None:
        checks = []

    return test.cmd('az confidentialledger create '
             '--location "EastUS" '
             '--aad-based-security-principals ledger-role-name="Administrator" principal-id="34621747-6fc8-4771-a2eb-72'
             'f31c461f2e" tenant-id="bce123b9-2b7b-4975-8360-5ca0b9b1cd08" '
             '--cert-based-security-principals cert="-----BEGIN CERTIFICATE-----MIIBsjCCATigAwIBAgIUZWIbyG79TniQLd2UxJu'
             'U74tqrKcwCgYIKoZIzj0EAwMwEDEOMAwGA1UEAwwFdXNlcjAwHhcNMjEwMzE2MTgwNjExWhcNMjIwMzE2MTgwNjExWjAQMQ4wDAYDVQQD'
             'DAV1c2VyMDB2MBAGByqGSM49AgEGBSuBBAAiA2IABBiWSo/j8EFit7aUMm5lF+lUmCu+IgfnpFD+7QMgLKtxRJ3aGSqgS/GpqcYVGddnO'
             'DtSarNE/HyGKUFUolLPQ5ybHcouUk0kyfA7XMeSoUA4lBz63Wha8wmXo+NdBRo39qNTMFEwHQYDVR0OBBYEFPtuhrwgGjDFHeUUT4nGsX'
             'aZn69KMB8GA1UdIwQYMBaAFPtuhrwgGjDFHeUUT4nGsXaZn69KMA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwMDaAAwZQIxAOnozm2'
             'CyqRwSSQLls5r+mUHRGRyXHXwYtM4Dcst/VEZdmS9fqvHRCHbjUlO/+HNfgIwMWZ4FmsjD3wnPxONOm9YdVn/PRD7SsPRPbOjwBiE4EBG'
             'aHDsLjYAGDSGi7NJnSkA-----END CERTIFICATE-----" ledger-role-name="Reader" '
             '--ledger-type "Public" '
             '--tags additionalProps1="additional properties" '
             '--name "{myLedger}" '
             '--resource-group "{rg}"',
             checks=[])

    # The `create` command already waits for resource creation. Testing the `wait` command
    # results in an infinite loop of GET resource -> 200 OK.


# EXAMPLE: /Ledger/get/ConfidentialLedgerGet
@try_manual
def step_show(test, checks=None):
    if checks is None:
        checks = []
    return test.cmd('az confidentialledger show '
                              '--name "{myLedger}" '
                              '--resource-group "{rg}"',
                               checks=checks)


# EXAMPLE: /Ledger/get/ConfidentialLedgerList
@try_manual
def step_list_by_resource_group(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az confidentialledger list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Ledger/get/ConfidentialLedgerListBySub
@try_manual
def step_list_by_subscription(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az confidentialledger list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Ledger/patch/ConfidentialLedgerUpdate
@try_manual
def step_update(test, create_output_json, checks=None):
    if checks is None:
        checks = []

    aad_based_principals = ""
    for aad_principal in create_output_json["properties"]["aadBasedSecurityPrincipals"]:
        if len(aad_based_principals) == 0:
            aad_based_principals = "--aad-based-security-principals"

        role_name = aad_principal["ledgerRoleName"]
        principal_id = aad_principal["principalId"]
        tenant_id = aad_principal["tenantId"]
        aad_based_principals += (
            f' ledger-role-name="{role_name}" principal-id="{principal_id}" tenant-id="{tenant_id}"'
        )

    cert_based_principals = ""
    for cert_based_principal in create_output_json["properties"]["certBasedSecurityPrincipals"]:
        if len(cert_based_principals) == 0:
            cert_based_principals = "--cert-based-security-principals"

        cert = cert_based_principal["cert"]
        role_name = cert_based_principal["ledgerRoleName"]
        cert_based_principals += (
            f' cert="{cert}" ledger-role-name="{role_name}"'
        )

    location = create_output_json["location"]
    ledger_type = create_output_json["properties"]["ledgerType"]

    tags = 'additionProps2="additional property value"'
    for key, value in create_output_json["tags"].items():
        tags += f' {key}="{value}"'

    test.cmd('az confidentialledger update '
             f'--location "{location}" '
             f'{aad_based_principals} '
             f'{cert_based_principals} '
             f'--ledger-type "{ledger_type}" '
             f'--tags {tags} '
             '--location "EastUS" '
             '--name "{myLedger}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Ledger/delete/ConfidentialLedgerDelete
@try_manual
def step_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az confidentialledger delete -y '
             '--name "{myLedger}" '
             '--resource-group "{rg}"',
             checks=checks)