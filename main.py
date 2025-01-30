from justorservice import Logger, __version__, env

if __name__ == '__main__':
    Logger.info(f'Started JustOR-Service {__version__}')
    Logger.info('Thank you for using, JustOR-Service ♥')

    token = str(env('APP_TOKEN')).strip()
    items = token.split('.')

    # A valid token should contains 2 dots and 3 items
    if len(items) != 3:
        Logger.critical('please change ATOKEN in .ENV, to a valid token.')
        exit(1)

    hmac_hide = '*' * len(items[2])  # Hide the secret
    Logger.debug(f'Static token: {items[0]}.{items[1]}.{hmac_hide}')

    # Run the bot
    from justorservice.main import client, exit_signal
    client.run(token)

    exit_signal.set()
    Logger.info('Stopping JustOR-Service..')
