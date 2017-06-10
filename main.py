from migrations.migration_executor import MigrationExecutor


def run(name, code):
    pass


if __name__ == '__main__':
    migration = MigrationExecutor()
    migration.start()
    # print("insert the provider name")
    # provider_name = input()
    # print("insert the provider code")
    # provider_code = input()
    # result = run(provider_name, provider_code)
    # print(result)
