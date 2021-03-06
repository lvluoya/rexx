

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chain.proto',
  package='protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x63hain.proto\x12\x08protocol\x1a\x0c\x63ommon.proto\"\xb7\x01\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05nonce\x18\x02 \x01(\x03\x12(\n\x04priv\x18\x03 \x01(\x0b\x32\x1a.protocol.AccountPrivilege\x12\x16\n\x0emetadatas_hash\x18\x04 \x01(\x0c\x12\x13\n\x0b\x61ssets_hash\x18\x05 \x01(\x0c\x12$\n\x08\x63ontract\x18\x06 \x01(\x0b\x32\x12.protocol.Contract\x12\x0f\n\x07\x62\x61lance\x18\x07 \x01(\x03\"6\n\x08\x41ssetKey\x12\x0e\n\x06issuer\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\"8\n\x05\x41sset\x12\x1f\n\x03key\x18\x01 \x01(\x0b\x32\x12.protocol.AssetKey\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"u\n\rAssetProperty\x12\x0f\n\x07\x64\x65\x63imal\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nmax_supply\x18\x03 \x01(\x03\x12\x15\n\rissued_amount\x18\x04 \x01(\x03\x12\x13\n\x0b\x66\x65\x65_percent\x18\x05 \x01(\x05\"h\n\nAssetStore\x12\x1f\n\x03key\x18\x01 \x01(\x0b\x32\x12.protocol.AssetKey\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12)\n\x08property\x18\x03 \x01(\x0b\x32\x17.protocol.AssetProperty\"\xed\x01\n\x0cLedgerHeader\x12\x0b\n\x03seq\x18\x01 \x01(\x03\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x15\n\rprevious_hash\x18\x03 \x01(\x0c\x12\x19\n\x11\x61\x63\x63ount_tree_hash\x18\x04 \x01(\x0c\x12\x12\n\nclose_time\x18\x05 \x01(\x03\x12\x1c\n\x14\x63onsensus_value_hash\x18\x06 \x01(\x0c\x12\x0f\n\x07version\x18\x07 \x01(\x03\x12\x10\n\x08tx_count\x18\x08 \x01(\x03\x12\x17\n\x0fvalidators_hash\x18\t \x01(\x0c\x12\x11\n\tfees_hash\x18\n \x01(\x0c\x12\x0f\n\x07reserve\x18\x0b \x01(\t\"d\n\x06Ledger\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.protocol.LedgerHeader\x12\x32\n\x10transaction_envs\x18\x02 \x03(\x0b\x32\x18.protocol.TransactionEnv\"X\n\x11OperationPayAsset\x12\x14\n\x0c\x64\x65st_address\x18\x01 \x01(\t\x12\x1e\n\x05\x61sset\x18\x02 \x01(\x0b\x32\x0f.protocol.Asset\x12\r\n\x05input\x18\x03 \x01(\t\"S\n\x16OperationTypeThreshold\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.protocol.Operation.Type\x12\x11\n\tthreshold\x18\x02 \x01(\x03\"|\n\x10\x41\x63\x63ountPrivilege\x12\x15\n\rmaster_weight\x18\x01 \x01(\x03\x12!\n\x07signers\x18\x02 \x03(\x0b\x32\x10.protocol.Signer\x12.\n\nthresholds\x18\x03 \x01(\x0b\x32\x1a.protocol.AccountThreshold\"c\n\x10\x41\x63\x63ountThreshold\x12\x14\n\x0ctx_threshold\x18\x01 \x01(\x03\x12\x39\n\x0ftype_thresholds\x18\x02 \x03(\x0b\x32 .protocol.OperationTypeThreshold\"3\n\x13OperationIssueAsset\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"G\n\x10OperationPayCoin\x12\x14\n\x0c\x64\x65st_address\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\r\n\x05input\x18\x03 \x01(\t\"T\n\x18OperationSetSignerWeight\x12\x15\n\rmaster_weight\x18\x01 \x01(\x03\x12!\n\x07signers\x18\x02 \x03(\x0b\x32\x10.protocol.Signer\",\n\x0cOperationLog\x12\r\n\x05topic\x18\x01 \x01(\t\x12\r\n\x05\x64\x61tas\x18\x02 \x03(\t\"\xa2\x01\n\x15OperationSetPrivilege\x12\x15\n\rmaster_weight\x18\x01 \x01(\t\x12!\n\x07signers\x18\x02 \x03(\x0b\x32\x10.protocol.Signer\x12\x14\n\x0ctx_threshold\x18\x03 \x01(\t\x12\x39\n\x0ftype_thresholds\x18\x04 \x03(\x0b\x32 .protocol.OperationTypeThreshold\"\xe3\x05\n\tOperation\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.protocol.Operation.Type\x12\x16\n\x0esource_address\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\x0c\x12\x38\n\x0e\x63reate_account\x18\x04 \x01(\x0b\x32 .protocol.OperationCreateAccount\x12\x32\n\x0bissue_asset\x18\x05 \x01(\x0b\x32\x1d.protocol.OperationIssueAsset\x12.\n\tpay_asset\x18\x06 \x01(\x0b\x32\x1b.protocol.OperationPayAsset\x12\x34\n\x0cset_metadata\x18\x07 \x01(\x0b\x32\x1e.protocol.OperationSetMetadata\x12=\n\x11set_signer_weight\x18\x08 \x01(\x0b\x32\".protocol.OperationSetSignerWeight\x12\x36\n\rset_threshold\x18\t \x01(\x0b\x32\x1f.protocol.OperationSetThreshold\x12,\n\x08pay_coin\x18\n \x01(\x0b\x32\x1a.protocol.OperationPayCoin\x12#\n\x03log\x18\x0b \x01(\x0b\x32\x16.protocol.OperationLog\x12\x36\n\rset_privilege\x18\x0c \x01(\x0b\x32\x1f.protocol.OperationSetPrivilege\"\xad\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0e\x43REATE_ACCOUNT\x10\x01\x12\x0f\n\x0bISSUE_ASSET\x10\x02\x12\r\n\tPAY_ASSET\x10\x03\x12\x10\n\x0cSET_METADATA\x10\x04\x12\x15\n\x11SET_SIGNER_WEIGHT\x10\x05\x12\x11\n\rSET_THRESHOLD\x10\x06\x12\x0c\n\x08PAY_COIN\x10\x07\x12\x07\n\x03LOG\x10\x08\x12\x11\n\rSET_PRIVILEGE\x10\t\"h\n\x15OperationSetThreshold\x12\x14\n\x0ctx_threshold\x18\x01 \x01(\x03\x12\x39\n\x0ftype_thresholds\x18\x02 \x03(\x0b\x32 .protocol.OperationTypeThreshold\"\xd5\x01\n\x0bTransaction\x12\x16\n\x0esource_address\x18\x01 \x01(\t\x12\r\n\x05nonce\x18\x02 \x01(\x03\x12\x11\n\tfee_limit\x18\x03 \x01(\x03\x12\x11\n\tgas_price\x18\x04 \x01(\x03\x12\x17\n\x0f\x63\x65il_ledger_seq\x18\x05 \x01(\x03\x12\x10\n\x08metadata\x18\x06 \x01(\x0c\x12\'\n\noperations\x18\x07 \x03(\x0b\x32\x13.protocol.Operation\"%\n\x05Limit\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\nOPERATIONS\x10\xe8\x07\"O\n\x06Signer\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\x03\"$\n\x05Limit\x12\x0f\n\x0bSIGNER_NONE\x10\x00\x12\n\n\x06SIGNER\x10\x64\"\x89\x02\n\x07Trigger\x12;\n\x10transaction_type\x18\x01 \x01(\x0e\x32!.protocol.Trigger.TransactionType\x12\x12\n\nledger_seq\x18\x02 \x01(\x03\x12\x37\n\x0btransaction\x18\x03 \x01(\x0b\x32\".protocol.Trigger.OperationTrigger\x1a/\n\x10OperationTrigger\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\x03\"C\n\x0fTransactionType\x12\x16\n\x12NORMAL_TRANSACTION\x10\x00\x12\x18\n\x14\x43ONTRACT_TRANSACTION\x10\x01\"\x89\x01\n\x0eTransactionEnv\x12*\n\x0btransaction\x18\x01 \x01(\x0b\x32\x15.protocol.Transaction\x12\'\n\nsignatures\x18\x02 \x03(\x0b\x32\x13.protocol.Signature\x12\"\n\x07trigger\x18\x03 \x01(\x0b\x32\x11.protocol.Trigger\"\xba\x01\n\x13TransactionEnvStore\x12\x31\n\x0ftransaction_env\x18\x01 \x01(\x0b\x32\x18.protocol.TransactionEnv\x12\x12\n\nerror_code\x18\x02 \x01(\x05\x12\x12\n\nerror_desc\x18\x03 \x01(\t\x12\x12\n\nledger_seq\x18\x04 \x01(\x03\x12\x12\n\nclose_time\x18\x05 \x01(\x03\x12\x0c\n\x04hash\x18\x06 \x01(\x0c\x12\x12\n\nactual_fee\x18\x07 \x01(\x03\":\n\x11TransactionEnvSet\x12%\n\x03txs\x18\x02 \x03(\x0b\x32\x18.protocol.TransactionEnv\"G\n\x18\x43onsensusValueValidation\x12\x15\n\rexpire_tx_ids\x18\x01 \x03(\x05\x12\x14\n\x0c\x65rror_tx_ids\x18\x02 \x03(\x05\"\x83\x02\n\x0e\x43onsensusValue\x12*\n\x05txset\x18\x01 \x01(\x0b\x32\x1b.protocol.TransactionEnvSet\x12\x12\n\nclose_time\x18\x02 \x01(\x03\x12\x16\n\x0eprevious_proof\x18\x03 \x01(\x0c\x12\x12\n\nledger_seq\x18\x04 \x01(\x03\x12\x1c\n\x14previous_ledger_hash\x18\x05 \x01(\x0c\x12/\n\x0eledger_upgrade\x18\x06 \x01(\x0b\x32\x17.protocol.LedgerUpgrade\x12\x36\n\nvalidation\x18\x07 \x01(\x0b\x32\".protocol.ConsensusValueValidation\"j\n\x08\x43ontract\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.protocol.Contract.ContractType\x12\x0f\n\x07payload\x18\x02 \x01(\t\"\x1e\n\x0c\x43ontractType\x12\x0e\n\nJAVASCRIPT\x10\x00\"\xce\x01\n\x16OperationCreateAccount\x12\x14\n\x0c\x64\x65st_address\x18\x01 \x01(\t\x12$\n\x08\x63ontract\x18\x02 \x01(\x0b\x32\x12.protocol.Contract\x12(\n\x04priv\x18\x03 \x01(\x0b\x32\x1a.protocol.AccountPrivilege\x12$\n\tmetadatas\x18\x04 \x03(\x0b\x32\x11.protocol.KeyPair\x12\x14\n\x0cinit_balance\x18\x05 \x01(\x03\x12\x12\n\ninit_input\x18\x06 \x01(\t\"X\n\x14OperationSetMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x13\n\x0b\x64\x65lete_flag\x18\x04 \x01(\x08*#\n\x05Limit\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tSIGNATURE\x10\x64\x42\"\n io.rexx.sdk.core.extend.protobufb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_LIMIT = _descriptor.EnumDescriptor(
  name='Limit',
  full_name='protocol.Limit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGNATURE', index=1, number=100,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=4275,
  serialized_end=4310,
)
_sym_db.RegisterEnumDescriptor(_LIMIT)

Limit = enum_type_wrapper.EnumTypeWrapper(_LIMIT)
UNKNOWN = 0
SIGNATURE = 100


_OPERATION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='protocol.Operation.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_ACCOUNT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISSUE_ASSET', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAY_ASSET', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_METADATA', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_SIGNER_WEIGHT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_THRESHOLD', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAY_COIN', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_PRIVILEGE', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2298,
  serialized_end=2471,
)
_sym_db.RegisterEnumDescriptor(_OPERATION_TYPE)

_TRANSACTION_LIMIT = _descriptor.EnumDescriptor(
  name='Limit',
  full_name='protocol.Transaction.Limit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATIONS', index=1, number=1000,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2756,
  serialized_end=2793,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTION_LIMIT)

_SIGNER_LIMIT = _descriptor.EnumDescriptor(
  name='Limit',
  full_name='protocol.Signer.Limit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIGNER_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGNER', index=1, number=100,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2838,
  serialized_end=2874,
)
_sym_db.RegisterEnumDescriptor(_SIGNER_LIMIT)

_TRIGGER_TRANSACTIONTYPE = _descriptor.EnumDescriptor(
  name='TransactionType',
  full_name='protocol.Trigger.TransactionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL_TRANSACTION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTRACT_TRANSACTION', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=3075,
  serialized_end=3142,
)
_sym_db.RegisterEnumDescriptor(_TRIGGER_TRANSACTIONTYPE)

_CONTRACT_CONTRACTTYPE = _descriptor.EnumDescriptor(
  name='ContractType',
  full_name='protocol.Contract.ContractType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JAVASCRIPT', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=3944,
  serialized_end=3974,
)
_sym_db.RegisterEnumDescriptor(_CONTRACT_CONTRACTTYPE)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='protocol.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='protocol.Account.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='protocol.Account.nonce', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priv', full_name='protocol.Account.priv', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadatas_hash', full_name='protocol.Account.metadatas_hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assets_hash', full_name='protocol.Account.assets_hash', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract', full_name='protocol.Account.contract', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='protocol.Account.balance', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=223,
)


_ASSETKEY = _descriptor.Descriptor(
  name='AssetKey',
  full_name='protocol.AssetKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issuer', full_name='protocol.AssetKey.issuer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='protocol.AssetKey.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.AssetKey.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=279,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='protocol.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Asset.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protocol.Asset.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=337,
)


_ASSETPROPERTY = _descriptor.Descriptor(
  name='AssetProperty',
  full_name='protocol.AssetProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='decimal', full_name='protocol.AssetProperty.decimal', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='protocol.AssetProperty.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_supply', full_name='protocol.AssetProperty.max_supply', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issued_amount', full_name='protocol.AssetProperty.issued_amount', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_percent', full_name='protocol.AssetProperty.fee_percent', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=456,
)


_ASSETSTORE = _descriptor.Descriptor(
  name='AssetStore',
  full_name='protocol.AssetStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.AssetStore.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protocol.AssetStore.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='property', full_name='protocol.AssetStore.property', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=562,
)


_LEDGERHEADER = _descriptor.Descriptor(
  name='LedgerHeader',
  full_name='protocol.LedgerHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='protocol.LedgerHeader.seq', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='protocol.LedgerHeader.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_hash', full_name='protocol.LedgerHeader.previous_hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_tree_hash', full_name='protocol.LedgerHeader.account_tree_hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_time', full_name='protocol.LedgerHeader.close_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consensus_value_hash', full_name='protocol.LedgerHeader.consensus_value_hash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='protocol.LedgerHeader.version', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_count', full_name='protocol.LedgerHeader.tx_count', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators_hash', full_name='protocol.LedgerHeader.validators_hash', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fees_hash', full_name='protocol.LedgerHeader.fees_hash', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserve', full_name='protocol.LedgerHeader.reserve', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=802,
)


_LEDGER = _descriptor.Descriptor(
  name='Ledger',
  full_name='protocol.Ledger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='protocol.Ledger.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_envs', full_name='protocol.Ledger.transaction_envs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=904,
)


_OPERATIONPAYASSET = _descriptor.Descriptor(
  name='OperationPayAsset',
  full_name='protocol.OperationPayAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dest_address', full_name='protocol.OperationPayAsset.dest_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset', full_name='protocol.OperationPayAsset.asset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='protocol.OperationPayAsset.input', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=994,
)


_OPERATIONTYPETHRESHOLD = _descriptor.Descriptor(
  name='OperationTypeThreshold',
  full_name='protocol.OperationTypeThreshold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.OperationTypeThreshold.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='protocol.OperationTypeThreshold.threshold', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=996,
  serialized_end=1079,
)


_ACCOUNTPRIVILEGE = _descriptor.Descriptor(
  name='AccountPrivilege',
  full_name='protocol.AccountPrivilege',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='master_weight', full_name='protocol.AccountPrivilege.master_weight', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signers', full_name='protocol.AccountPrivilege.signers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thresholds', full_name='protocol.AccountPrivilege.thresholds', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1081,
  serialized_end=1205,
)


_ACCOUNTTHRESHOLD = _descriptor.Descriptor(
  name='AccountThreshold',
  full_name='protocol.AccountThreshold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_threshold', full_name='protocol.AccountThreshold.tx_threshold', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_thresholds', full_name='protocol.AccountThreshold.type_thresholds', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1207,
  serialized_end=1306,
)


_OPERATIONISSUEASSET = _descriptor.Descriptor(
  name='OperationIssueAsset',
  full_name='protocol.OperationIssueAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='protocol.OperationIssueAsset.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protocol.OperationIssueAsset.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1308,
  serialized_end=1359,
)


_OPERATIONPAYCOIN = _descriptor.Descriptor(
  name='OperationPayCoin',
  full_name='protocol.OperationPayCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dest_address', full_name='protocol.OperationPayCoin.dest_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protocol.OperationPayCoin.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='protocol.OperationPayCoin.input', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1361,
  serialized_end=1432,
)


_OPERATIONSETSIGNERWEIGHT = _descriptor.Descriptor(
  name='OperationSetSignerWeight',
  full_name='protocol.OperationSetSignerWeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='master_weight', full_name='protocol.OperationSetSignerWeight.master_weight', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signers', full_name='protocol.OperationSetSignerWeight.signers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1434,
  serialized_end=1518,
)


_OPERATIONLOG = _descriptor.Descriptor(
  name='OperationLog',
  full_name='protocol.OperationLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='protocol.OperationLog.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datas', full_name='protocol.OperationLog.datas', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1520,
  serialized_end=1564,
)


_OPERATIONSETPRIVILEGE = _descriptor.Descriptor(
  name='OperationSetPrivilege',
  full_name='protocol.OperationSetPrivilege',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='master_weight', full_name='protocol.OperationSetPrivilege.master_weight', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signers', full_name='protocol.OperationSetPrivilege.signers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_threshold', full_name='protocol.OperationSetPrivilege.tx_threshold', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_thresholds', full_name='protocol.OperationSetPrivilege.type_thresholds', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1567,
  serialized_end=1729,
)


_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='protocol.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.Operation.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_address', full_name='protocol.Operation.source_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='protocol.Operation.metadata', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_account', full_name='protocol.Operation.create_account', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue_asset', full_name='protocol.Operation.issue_asset', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_asset', full_name='protocol.Operation.pay_asset', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_metadata', full_name='protocol.Operation.set_metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_signer_weight', full_name='protocol.Operation.set_signer_weight', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_threshold', full_name='protocol.Operation.set_threshold', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_coin', full_name='protocol.Operation.pay_coin', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='protocol.Operation.log', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_privilege', full_name='protocol.Operation.set_privilege', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPERATION_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1732,
  serialized_end=2471,
)


_OPERATIONSETTHRESHOLD = _descriptor.Descriptor(
  name='OperationSetThreshold',
  full_name='protocol.OperationSetThreshold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_threshold', full_name='protocol.OperationSetThreshold.tx_threshold', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_thresholds', full_name='protocol.OperationSetThreshold.type_thresholds', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2473,
  serialized_end=2577,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='protocol.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_address', full_name='protocol.Transaction.source_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='protocol.Transaction.nonce', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_limit', full_name='protocol.Transaction.fee_limit', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_price', full_name='protocol.Transaction.gas_price', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ceil_ledger_seq', full_name='protocol.Transaction.ceil_ledger_seq', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='protocol.Transaction.metadata', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='protocol.Transaction.operations', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSACTION_LIMIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2580,
  serialized_end=2793,
)


_SIGNER = _descriptor.Descriptor(
  name='Signer',
  full_name='protocol.Signer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='protocol.Signer.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='protocol.Signer.weight', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIGNER_LIMIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2795,
  serialized_end=2874,
)


_TRIGGER_OPERATIONTRIGGER = _descriptor.Descriptor(
  name='OperationTrigger',
  full_name='protocol.Trigger.OperationTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='protocol.Trigger.OperationTrigger.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='protocol.Trigger.OperationTrigger.index', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3026,
  serialized_end=3073,
)

_TRIGGER = _descriptor.Descriptor(
  name='Trigger',
  full_name='protocol.Trigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_type', full_name='protocol.Trigger.transaction_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_seq', full_name='protocol.Trigger.ledger_seq', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction', full_name='protocol.Trigger.transaction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRIGGER_OPERATIONTRIGGER, ],
  enum_types=[
    _TRIGGER_TRANSACTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2877,
  serialized_end=3142,
)


_TRANSACTIONENV = _descriptor.Descriptor(
  name='TransactionEnv',
  full_name='protocol.TransactionEnv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='protocol.TransactionEnv.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='protocol.TransactionEnv.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='protocol.TransactionEnv.trigger', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3145,
  serialized_end=3282,
)


_TRANSACTIONENVSTORE = _descriptor.Descriptor(
  name='TransactionEnvStore',
  full_name='protocol.TransactionEnvStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_env', full_name='protocol.TransactionEnvStore.transaction_env', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='protocol.TransactionEnvStore.error_code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_desc', full_name='protocol.TransactionEnvStore.error_desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_seq', full_name='protocol.TransactionEnvStore.ledger_seq', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_time', full_name='protocol.TransactionEnvStore.close_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='protocol.TransactionEnvStore.hash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_fee', full_name='protocol.TransactionEnvStore.actual_fee', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3285,
  serialized_end=3471,
)


_TRANSACTIONENVSET = _descriptor.Descriptor(
  name='TransactionEnvSet',
  full_name='protocol.TransactionEnvSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txs', full_name='protocol.TransactionEnvSet.txs', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3473,
  serialized_end=3531,
)


_CONSENSUSVALUEVALIDATION = _descriptor.Descriptor(
  name='ConsensusValueValidation',
  full_name='protocol.ConsensusValueValidation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='expire_tx_ids', full_name='protocol.ConsensusValueValidation.expire_tx_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_tx_ids', full_name='protocol.ConsensusValueValidation.error_tx_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3533,
  serialized_end=3604,
)


_CONSENSUSVALUE = _descriptor.Descriptor(
  name='ConsensusValue',
  full_name='protocol.ConsensusValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txset', full_name='protocol.ConsensusValue.txset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_time', full_name='protocol.ConsensusValue.close_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_proof', full_name='protocol.ConsensusValue.previous_proof', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_seq', full_name='protocol.ConsensusValue.ledger_seq', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_ledger_hash', full_name='protocol.ConsensusValue.previous_ledger_hash', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_upgrade', full_name='protocol.ConsensusValue.ledger_upgrade', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validation', full_name='protocol.ConsensusValue.validation', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3607,
  serialized_end=3866,
)


_CONTRACT = _descriptor.Descriptor(
  name='Contract',
  full_name='protocol.Contract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.Contract.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protocol.Contract.payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTRACT_CONTRACTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3868,
  serialized_end=3974,
)


_OPERATIONCREATEACCOUNT = _descriptor.Descriptor(
  name='OperationCreateAccount',
  full_name='protocol.OperationCreateAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dest_address', full_name='protocol.OperationCreateAccount.dest_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract', full_name='protocol.OperationCreateAccount.contract', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priv', full_name='protocol.OperationCreateAccount.priv', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadatas', full_name='protocol.OperationCreateAccount.metadatas', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_balance', full_name='protocol.OperationCreateAccount.init_balance', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_input', full_name='protocol.OperationCreateAccount.init_input', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3977,
  serialized_end=4183,
)


_OPERATIONSETMETADATA = _descriptor.Descriptor(
  name='OperationSetMetadata',
  full_name='protocol.OperationSetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.OperationSetMetadata.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.OperationSetMetadata.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='protocol.OperationSetMetadata.version', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_flag', full_name='protocol.OperationSetMetadata.delete_flag', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4185,
  serialized_end=4273,
)

_ACCOUNT.fields_by_name['priv'].message_type = _ACCOUNTPRIVILEGE
_ACCOUNT.fields_by_name['contract'].message_type = _CONTRACT
_ASSET.fields_by_name['key'].message_type = _ASSETKEY
_ASSETSTORE.fields_by_name['key'].message_type = _ASSETKEY
_ASSETSTORE.fields_by_name['property'].message_type = _ASSETPROPERTY
_LEDGER.fields_by_name['header'].message_type = _LEDGERHEADER
_LEDGER.fields_by_name['transaction_envs'].message_type = _TRANSACTIONENV
_OPERATIONPAYASSET.fields_by_name['asset'].message_type = _ASSET
_OPERATIONTYPETHRESHOLD.fields_by_name['type'].enum_type = _OPERATION_TYPE
_ACCOUNTPRIVILEGE.fields_by_name['signers'].message_type = _SIGNER
_ACCOUNTPRIVILEGE.fields_by_name['thresholds'].message_type = _ACCOUNTTHRESHOLD
_ACCOUNTTHRESHOLD.fields_by_name['type_thresholds'].message_type = _OPERATIONTYPETHRESHOLD
_OPERATIONSETSIGNERWEIGHT.fields_by_name['signers'].message_type = _SIGNER
_OPERATIONSETPRIVILEGE.fields_by_name['signers'].message_type = _SIGNER
_OPERATIONSETPRIVILEGE.fields_by_name['type_thresholds'].message_type = _OPERATIONTYPETHRESHOLD
_OPERATION.fields_by_name['type'].enum_type = _OPERATION_TYPE
_OPERATION.fields_by_name['create_account'].message_type = _OPERATIONCREATEACCOUNT
_OPERATION.fields_by_name['issue_asset'].message_type = _OPERATIONISSUEASSET
_OPERATION.fields_by_name['pay_asset'].message_type = _OPERATIONPAYASSET
_OPERATION.fields_by_name['set_metadata'].message_type = _OPERATIONSETMETADATA
_OPERATION.fields_by_name['set_signer_weight'].message_type = _OPERATIONSETSIGNERWEIGHT
_OPERATION.fields_by_name['set_threshold'].message_type = _OPERATIONSETTHRESHOLD
_OPERATION.fields_by_name['pay_coin'].message_type = _OPERATIONPAYCOIN
_OPERATION.fields_by_name['log'].message_type = _OPERATIONLOG
_OPERATION.fields_by_name['set_privilege'].message_type = _OPERATIONSETPRIVILEGE
_OPERATION_TYPE.containing_type = _OPERATION
_OPERATIONSETTHRESHOLD.fields_by_name['type_thresholds'].message_type = _OPERATIONTYPETHRESHOLD
_TRANSACTION.fields_by_name['operations'].message_type = _OPERATION
_TRANSACTION_LIMIT.containing_type = _TRANSACTION
_SIGNER_LIMIT.containing_type = _SIGNER
_TRIGGER_OPERATIONTRIGGER.containing_type = _TRIGGER
_TRIGGER.fields_by_name['transaction_type'].enum_type = _TRIGGER_TRANSACTIONTYPE
_TRIGGER.fields_by_name['transaction'].message_type = _TRIGGER_OPERATIONTRIGGER
_TRIGGER_TRANSACTIONTYPE.containing_type = _TRIGGER
_TRANSACTIONENV.fields_by_name['transaction'].message_type = _TRANSACTION
_TRANSACTIONENV.fields_by_name['signatures'].message_type = common__pb2._SIGNATURE
_TRANSACTIONENV.fields_by_name['trigger'].message_type = _TRIGGER
_TRANSACTIONENVSTORE.fields_by_name['transaction_env'].message_type = _TRANSACTIONENV
_TRANSACTIONENVSET.fields_by_name['txs'].message_type = _TRANSACTIONENV
_CONSENSUSVALUE.fields_by_name['txset'].message_type = _TRANSACTIONENVSET
_CONSENSUSVALUE.fields_by_name['ledger_upgrade'].message_type = common__pb2._LEDGERUPGRADE
_CONSENSUSVALUE.fields_by_name['validation'].message_type = _CONSENSUSVALUEVALIDATION
_CONTRACT.fields_by_name['type'].enum_type = _CONTRACT_CONTRACTTYPE
_CONTRACT_CONTRACTTYPE.containing_type = _CONTRACT
_OPERATIONCREATEACCOUNT.fields_by_name['contract'].message_type = _CONTRACT
_OPERATIONCREATEACCOUNT.fields_by_name['priv'].message_type = _ACCOUNTPRIVILEGE
_OPERATIONCREATEACCOUNT.fields_by_name['metadatas'].message_type = common__pb2._KEYPAIR
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['AssetKey'] = _ASSETKEY
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['AssetProperty'] = _ASSETPROPERTY
DESCRIPTOR.message_types_by_name['AssetStore'] = _ASSETSTORE
DESCRIPTOR.message_types_by_name['LedgerHeader'] = _LEDGERHEADER
DESCRIPTOR.message_types_by_name['Ledger'] = _LEDGER
DESCRIPTOR.message_types_by_name['OperationPayAsset'] = _OPERATIONPAYASSET
DESCRIPTOR.message_types_by_name['OperationTypeThreshold'] = _OPERATIONTYPETHRESHOLD
DESCRIPTOR.message_types_by_name['AccountPrivilege'] = _ACCOUNTPRIVILEGE
DESCRIPTOR.message_types_by_name['AccountThreshold'] = _ACCOUNTTHRESHOLD
DESCRIPTOR.message_types_by_name['OperationIssueAsset'] = _OPERATIONISSUEASSET
DESCRIPTOR.message_types_by_name['OperationPayCoin'] = _OPERATIONPAYCOIN
DESCRIPTOR.message_types_by_name['OperationSetSignerWeight'] = _OPERATIONSETSIGNERWEIGHT
DESCRIPTOR.message_types_by_name['OperationLog'] = _OPERATIONLOG
DESCRIPTOR.message_types_by_name['OperationSetPrivilege'] = _OPERATIONSETPRIVILEGE
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['OperationSetThreshold'] = _OPERATIONSETTHRESHOLD
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['Signer'] = _SIGNER
DESCRIPTOR.message_types_by_name['Trigger'] = _TRIGGER
DESCRIPTOR.message_types_by_name['TransactionEnv'] = _TRANSACTIONENV
DESCRIPTOR.message_types_by_name['TransactionEnvStore'] = _TRANSACTIONENVSTORE
DESCRIPTOR.message_types_by_name['TransactionEnvSet'] = _TRANSACTIONENVSET
DESCRIPTOR.message_types_by_name['ConsensusValueValidation'] = _CONSENSUSVALUEVALIDATION
DESCRIPTOR.message_types_by_name['ConsensusValue'] = _CONSENSUSVALUE
DESCRIPTOR.message_types_by_name['Contract'] = _CONTRACT
DESCRIPTOR.message_types_by_name['OperationCreateAccount'] = _OPERATIONCREATEACCOUNT
DESCRIPTOR.message_types_by_name['OperationSetMetadata'] = _OPERATIONSETMETADATA
DESCRIPTOR.enum_types_by_name['Limit'] = _LIMIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Account)
  ))
_sym_db.RegisterMessage(Account)

AssetKey = _reflection.GeneratedProtocolMessageType('AssetKey', (_message.Message,), dict(
  DESCRIPTOR = _ASSETKEY,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AssetKey)
  ))
_sym_db.RegisterMessage(AssetKey)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), dict(
  DESCRIPTOR = _ASSET,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Asset)
  ))
_sym_db.RegisterMessage(Asset)

AssetProperty = _reflection.GeneratedProtocolMessageType('AssetProperty', (_message.Message,), dict(
  DESCRIPTOR = _ASSETPROPERTY,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AssetProperty)
  ))
_sym_db.RegisterMessage(AssetProperty)

AssetStore = _reflection.GeneratedProtocolMessageType('AssetStore', (_message.Message,), dict(
  DESCRIPTOR = _ASSETSTORE,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AssetStore)
  ))
_sym_db.RegisterMessage(AssetStore)

LedgerHeader = _reflection.GeneratedProtocolMessageType('LedgerHeader', (_message.Message,), dict(
  DESCRIPTOR = _LEDGERHEADER,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.LedgerHeader)
  ))
_sym_db.RegisterMessage(LedgerHeader)

Ledger = _reflection.GeneratedProtocolMessageType('Ledger', (_message.Message,), dict(
  DESCRIPTOR = _LEDGER,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Ledger)
  ))
_sym_db.RegisterMessage(Ledger)

OperationPayAsset = _reflection.GeneratedProtocolMessageType('OperationPayAsset', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONPAYASSET,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationPayAsset)
  ))
_sym_db.RegisterMessage(OperationPayAsset)

OperationTypeThreshold = _reflection.GeneratedProtocolMessageType('OperationTypeThreshold', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONTYPETHRESHOLD,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationTypeThreshold)
  ))
_sym_db.RegisterMessage(OperationTypeThreshold)

AccountPrivilege = _reflection.GeneratedProtocolMessageType('AccountPrivilege', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTPRIVILEGE,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AccountPrivilege)
  ))
_sym_db.RegisterMessage(AccountPrivilege)

AccountThreshold = _reflection.GeneratedProtocolMessageType('AccountThreshold', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTTHRESHOLD,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AccountThreshold)
  ))
_sym_db.RegisterMessage(AccountThreshold)

OperationIssueAsset = _reflection.GeneratedProtocolMessageType('OperationIssueAsset', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONISSUEASSET,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationIssueAsset)
  ))
_sym_db.RegisterMessage(OperationIssueAsset)

OperationPayCoin = _reflection.GeneratedProtocolMessageType('OperationPayCoin', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONPAYCOIN,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationPayCoin)
  ))
_sym_db.RegisterMessage(OperationPayCoin)

OperationSetSignerWeight = _reflection.GeneratedProtocolMessageType('OperationSetSignerWeight', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONSETSIGNERWEIGHT,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationSetSignerWeight)
  ))
_sym_db.RegisterMessage(OperationSetSignerWeight)

OperationLog = _reflection.GeneratedProtocolMessageType('OperationLog', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONLOG,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationLog)
  ))
_sym_db.RegisterMessage(OperationLog)

OperationSetPrivilege = _reflection.GeneratedProtocolMessageType('OperationSetPrivilege', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONSETPRIVILEGE,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationSetPrivilege)
  ))
_sym_db.RegisterMessage(OperationSetPrivilege)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
  DESCRIPTOR = _OPERATION,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Operation)
  ))
_sym_db.RegisterMessage(Operation)

OperationSetThreshold = _reflection.GeneratedProtocolMessageType('OperationSetThreshold', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONSETTHRESHOLD,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationSetThreshold)
  ))
_sym_db.RegisterMessage(OperationSetThreshold)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

Signer = _reflection.GeneratedProtocolMessageType('Signer', (_message.Message,), dict(
  DESCRIPTOR = _SIGNER,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Signer)
  ))
_sym_db.RegisterMessage(Signer)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), dict(

  OperationTrigger = _reflection.GeneratedProtocolMessageType('OperationTrigger', (_message.Message,), dict(
    DESCRIPTOR = _TRIGGER_OPERATIONTRIGGER,
    __module__ = 'chain_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Trigger.OperationTrigger)
    ))
  ,
  DESCRIPTOR = _TRIGGER,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Trigger)
  ))
_sym_db.RegisterMessage(Trigger)
_sym_db.RegisterMessage(Trigger.OperationTrigger)

TransactionEnv = _reflection.GeneratedProtocolMessageType('TransactionEnv', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONENV,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.TransactionEnv)
  ))
_sym_db.RegisterMessage(TransactionEnv)

TransactionEnvStore = _reflection.GeneratedProtocolMessageType('TransactionEnvStore', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONENVSTORE,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.TransactionEnvStore)
  ))
_sym_db.RegisterMessage(TransactionEnvStore)

TransactionEnvSet = _reflection.GeneratedProtocolMessageType('TransactionEnvSet', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONENVSET,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.TransactionEnvSet)
  ))
_sym_db.RegisterMessage(TransactionEnvSet)

ConsensusValueValidation = _reflection.GeneratedProtocolMessageType('ConsensusValueValidation', (_message.Message,), dict(
  DESCRIPTOR = _CONSENSUSVALUEVALIDATION,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ConsensusValueValidation)
  ))
_sym_db.RegisterMessage(ConsensusValueValidation)

ConsensusValue = _reflection.GeneratedProtocolMessageType('ConsensusValue', (_message.Message,), dict(
  DESCRIPTOR = _CONSENSUSVALUE,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ConsensusValue)
  ))
_sym_db.RegisterMessage(ConsensusValue)

Contract = _reflection.GeneratedProtocolMessageType('Contract', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACT,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Contract)
  ))
_sym_db.RegisterMessage(Contract)

OperationCreateAccount = _reflection.GeneratedProtocolMessageType('OperationCreateAccount', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONCREATEACCOUNT,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationCreateAccount)
  ))
_sym_db.RegisterMessage(OperationCreateAccount)

OperationSetMetadata = _reflection.GeneratedProtocolMessageType('OperationSetMetadata', (_message.Message,), dict(
  DESCRIPTOR = _OPERATIONSETMETADATA,
  __module__ = 'chain_pb2'
  # @@protoc_insertion_point(class_scope:protocol.OperationSetMetadata)
  ))
_sym_db.RegisterMessage(OperationSetMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n io.rexx.sdk.core.extend.protobuf'))
# @@protoc_insertion_point(module_scope)
