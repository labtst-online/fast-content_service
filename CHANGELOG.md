# CHANGELOG


## v0.2.0 (2025-05-09)

### Bug Fixes

- Move python-semantic-release dependence to dev-dependencies
  ([`8e23516`](https://github.com/fotapol/fastboosty-content_service/commit/8e23516db1668ebc5fd34259ce62f00a92aa6d31))

- Refactor CD workflow to confirm CI success and streamline release process
  ([`64c3dd1`](https://github.com/fotapol/fastboosty-content_service/commit/64c3dd145810a56d250aee145dfb803b4e1cc643))

- Remove duplicate commit_version_number option from semantic release configuration
  ([`5fdc6a6`](https://github.com/fotapol/fastboosty-content_service/commit/5fdc6a6fdebb93392e8ef97304261f3be909b05d))

- Rename release job and add semantic release logging
  ([`82b771b`](https://github.com/fotapol/fastboosty-content_service/commit/82b771bd1bfbcb99d0f76ad0816c7bf8fdddd457))

- Simplify dependency sync step in CI workflow
  ([`2c4f677`](https://github.com/fotapol/fastboosty-content_service/commit/2c4f6778e00f80be681e7548cb2d9a332f030a64))

- Update Dockerfile and .dockerignore for improved dependency management and caching
  ([`8ab9e8e`](https://github.com/fotapol/fastboosty-content_service/commit/8ab9e8e63ab31d731582bdd73a93ef0a244e432c))

- Update pyproject.toml to reorganize dependencies and enhance semantic release configuration
  ([`5443a1b`](https://github.com/fotapol/fastboosty-content_service/commit/5443a1b91eee96774bf7749588aa28b9aaa4a3a1))

- Update semantic release job to use correct output variables and streamline steps. Use official
  semantic_release image for github actions
  ([`5f40e8a`](https://github.com/fotapol/fastboosty-content_service/commit/5f40e8a8b151d16e2b45f96cfff5164b65f182f0))

- Update version retrieval and clean up logging configuration in main.py
  ([`a3d949f`](https://github.com/fotapol/fastboosty-content_service/commit/a3d949f01db778be82aa20463025f80753755f5d))

### Chores

- Enhance semantic-release workflow with Git status and commit history logging for debugging
  ([`b1b480b`](https://github.com/fotapol/fastboosty-content_service/commit/b1b480b29cf07b82e7a43859fe664cfb0b5d3a80))

- Styling code using ruff formater
  ([`bc8d07c`](https://github.com/fotapol/fastboosty-content_service/commit/bc8d07cd54c8bb12baae40c9a935cdc39d39143c))

### Features

- Add Continuous Delivery workflow and update Continuous Integration workflow
  ([`0fd4ad9`](https://github.com/fotapol/fastboosty-content_service/commit/0fd4ad9bfd92de595a758429140c674f72064f53))

- Upgrade Python version to 3.13 and enhance Dockerfile for dependency installation
  ([`4664482`](https://github.com/fotapol/fastboosty-content_service/commit/46644820c8dc03397bbda922a16a79253b896743))


## v0.1.0 (2025-05-06)

### Bug Fixes

- Correct import path for CurrentUserUUID in endpoints.py
  ([`7ec7ea9`](https://github.com/fotapol/fastboosty-content_service/commit/7ec7ea9d0993d68e8b5bcce138b1356932ee31d5))

- Fix --verbose flag for semantic-release
  ([`83cced0`](https://github.com/fotapol/fastboosty-content_service/commit/83cced05b0c882eee14a1f4870e5068c29583cf3))

- Remove AUTH_SERVICE_URL from config and .env.sample
  ([`28326bd`](https://github.com/fotapol/fastboosty-content_service/commit/28326bd7e8c04ddb9b5f99e4503f59249bf41eb6))

- Update PostgreSQL version to 17 and upgrade version auth-lib
  ([`777779b`](https://github.com/fotapol/fastboosty-content_service/commit/777779bf8fe4ea4925953e167523069640f4f015))

### Features

- Add auth-lib dependency for authentication handling
  ([`7bfe766`](https://github.com/fotapol/fastboosty-content_service/commit/7bfe766662f20eafcdc976a8fe4344ed44537b13))

- Add CI workflow for testing with PostgreSQL and Python
  ([`e211848`](https://github.com/fotapol/fastboosty-content_service/commit/e21184802c8d966e37267ae3d1cf60a51b08a44c))

- Add initial .dockerignore file to exclude Python cache
  ([`43693cc`](https://github.com/fotapol/fastboosty-content_service/commit/43693cc6fd04f6a6e953ce59d2115afb591661c5))

- Add python-semantic-release package. Update main.py.
  ([`f4e293d`](https://github.com/fotapol/fastboosty-content_service/commit/f4e293d05f408451921644df51348bea2564c2a0))

- Comment current unused part
  ([`efa553f`](https://github.com/fotapol/fastboosty-content_service/commit/efa553fd49d8655c8ea64f18e467ad779369a18f))

- Remove deprecated import of CurrentUserUUID from dependencies and add new import from new package
  ([`31284f4`](https://github.com/fotapol/fastboosty-content_service/commit/31284f435d6c58b13facb7f766c98e8abdadbd5f))

- **content**: Add Dockerfile and entrypoint script for content service
  ([`44f97fc`](https://github.com/fotapol/fastboosty-content_service/commit/44f97fc4c362589e63a5ad97a816506b8862a835))

- **content**: Add initial post model, schemas, and Alembic migration setup
  ([`ead8c74`](https://github.com/fotapol/fastboosty-content_service/commit/ead8c74638b1dc15b18fe4e6a7e11983cc675ec1))

- **content**: Add README, Alembic script template, and API endpoints for post management
  ([`dd4d765`](https://github.com/fotapol/fastboosty-content_service/commit/dd4d765fc6b4382900281fbbdf75714ae74125f8))

- **content**: Initialize content service with database configuration and FastAPI setup
  ([`b2cb6f8`](https://github.com/fotapol/fastboosty-content_service/commit/b2cb6f88412133c0a5e80585f06458e89f19fdb9))

### Refactoring

- Code styling using ruff formater
  ([`89a40bb`](https://github.com/fotapol/fastboosty-content_service/commit/89a40bbad9144e8b4e8cba86ff24b9be643a1b25))
