Tethys Platform
===============

.. image:: https://github.com/tethysplatform/tethys/actions/workflows/tethys.yml/badge.svg
    :target: https://github.com/tethysplatform/tethys/actions
    :alt: Test Status

.. image:: https://coveralls.io/repos/github/tethysplatform/tethys/badge.svg
    :target: https://coveralls.io/github/tethysplatform/tethys
    :alt: Coverage Status


.. image:: https://readthedocs.org/projects/tethys-platform/badge/?version=stable
    :target: http://docs.tethysplatform.org/en/stable/?badge=stable
    :alt: Documentation Status

Tethys Platform provides both a development environment and a hosting environment for water resources web apps.

Documentation can be found here: `<http://docs.tethysplatform.org/>`_

## WSO2 configuration

Modify portal_config.yml and add these configuration
```
AUTHENTICATION_BACKENDS: ['tethys_services.backends.wso2.WSO2OAuth2']  
SOCIAL_AUTH_WSO2_HOSTNAME: <<sso hostname e.g: sso.example.com>>
SOCIAL_AUTH_WSO2_KEY: 
SOCIAL_AUTH_WSO2_SECRET: 
SOCIAL_AUTH_WSO2_SCOPE: ['openid']
```