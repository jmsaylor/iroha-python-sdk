from iroha import Iroha, IrohaGrpc
from iroha import IrohaCrypto
import keys
import os
from iroha.primitive_pb2 import can_set_my_account_detail

IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '127.0.0.1')
IROHA_PORT = os.getenv('IROHA_PORT', '50051')
ADMIN_ACCOUNT_ID = os.getenv('ADMIN_ACCOUNT_ID', 'admin@test')
ADMIN_PRIVATE_KEY = os.getenv('ADMIN_PRIVATE_KEY', keys.get_admin_key())

def create_domain_and_asset():
    commands = [iroha.command('CreateDomain', domain_id='hgf', default_role='user'),
                iroha.command('CreateAsset', asset_name='vrc', domain_id='hgf', precision=2)
                ]
    tx = IrohaCrypto.sign_transaction(iroha.transaction(commands), ADMIN_PRIVATE_KEY)
    net.send_tx(tx)
    for status in net.tx_status_stream(tx):
        print(status)

if __name__ == '__main__':
    user_private_key = IrohaCrypto.private_key()
    user_public_key = IrohaCrypto.derive_public_key(user_private_key)
    iroha = Iroha(ADMIN_ACCOUNT_ID)
    net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))

    create_domain_and_asset()