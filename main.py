from iroha import Iroha, IrohaGrpc
from iroha import IrohaCrypto
import keys
from iroha.primitive_pb2 import can_set_my_account_detail

if __name__ == '__main__':
    admin_private_key = keys.get_admin_key()
    user_private_key = IrohaCrypto.private_key()
    user_public_key = IrohaCrypto.derive_public_key(user_private_key)
    iroha = Iroha('admin@test')
    net = IrohaGrpc()