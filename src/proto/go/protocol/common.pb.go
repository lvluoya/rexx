

package protocol

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type ERRORCODE int32

const (
	ERRORCODE_ERRCODE_SUCCESS                        ERRORCODE = 0
	ERRORCODE_ERRCODE_INTERNAL_ERROR                 ERRORCODE = 1
	ERRORCODE_ERRCODE_INVALID_PARAMETER              ERRORCODE = 2
	ERRORCODE_ERRCODE_ALREADY_EXIST                  ERRORCODE = 3
	ERRORCODE_ERRCODE_NOT_EXIST                      ERRORCODE = 4
	ERRORCODE_ERRCODE_TX_TIMEOUT                     ERRORCODE = 5
	ERRORCODE_ERRCODE_ACCESS_DENIED                  ERRORCODE = 6
	ERRORCODE_ERRCODE_MATH_OVERFLOW                  ERRORCODE = 7
	ERRORCODE_ERRCODE_EXPR_CONDITION_RESULT_FALSE    ERRORCODE = 20
	ERRORCODE_ERRCODE_EXPR_CONDITION_SYNTAX_ERROR    ERRORCODE = 21
	ERRORCODE_ERRCODE_INVALID_PUBKEY                 ERRORCODE = 90
	ERRORCODE_ERRCODE_INVALID_PRIKEY                 ERRORCODE = 91
	ERRORCODE_ERRCODE_ASSET_INVALID                  ERRORCODE = 92
	ERRORCODE_ERRCODE_INVALID_SIGNATURE              ERRORCODE = 93
	ERRORCODE_ERRCODE_INVALID_ADDRESS                ERRORCODE = 94
	ERRORCODE_ERRCODE_MISSING_OPERATIONS             ERRORCODE = 97
	ERRORCODE_ERRCODE_TOO_MANY_OPERATIONS            ERRORCODE = 98
	ERRORCODE_ERRCODE_BAD_SEQUENCE                   ERRORCODE = 99
	ERRORCODE_ERRCODE_ACCOUNT_LOW_RESERVE            ERRORCODE = 100
	ERRORCODE_ERRCODE_ACCOUNT_SOURCEDEST_EQUAL       ERRORCODE = 101
	ERRORCODE_ERRCODE_ACCOUNT_DEST_EXIST             ERRORCODE = 102
	ERRORCODE_ERRCODE_ACCOUNT_NOT_EXIST              ERRORCODE = 103
	ERRORCODE_ERRCODE_ACCOUNT_ASSET_LOW_RESERVE      ERRORCODE = 104
	ERRORCODE_ERRCODE_ACCOUNT_ASSET_AMOUNT_TOO_LARGE ERRORCODE = 105
	ERRORCODE_ERRCODE_ACCOUNT_INIT_LOW_RESERVE       ERRORCODE = 106
	ERRORCODE_ERRCODE_FEE_NOT_ENOUGH                 ERRORCODE = 111
	ERRORCODE_ERRCODE_FEE_INVALID                    ERRORCODE = 112
	ERRORCODE_ERRCODE_OUT_OF_TXCACHE                 ERRORCODE = 114
	ERRORCODE_ERRCODE_WEIGHT_NOT_VALID               ERRORCODE = 120
	ERRORCODE_ERRCODE_THRESHOLD_NOT_VALID            ERRORCODE = 121
	ERRORCODE_ERRCODE_INVALID_DATAVERSION            ERRORCODE = 144
	ERRORCODE_ERRCODE_TX_SIZE_TOO_BIG                ERRORCODE = 146
	ERRORCODE_ERRCODE_CONTRACT_EXECUTE_FAIL          ERRORCODE = 151
	ERRORCODE_ERRCODE_CONTRACT_SYNTAX_ERROR          ERRORCODE = 152
	ERRORCODE_ERRCODE_CONTRACT_TOO_MANY_RECURSION    ERRORCODE = 153
	ERRORCODE_ERRCODE_CONTRACT_TOO_MANY_TRANSACTIONS ERRORCODE = 154
	ERRORCODE_ERRCODE_CONTRACT_EXECUTE_EXPIRED       ERRORCODE = 155
	ERRORCODE_ERRCODE_TX_INSERT_QUEUE_FAIL           ERRORCODE = 160
)

var ERRORCODE_name = map[int32]string{
	0:   "ERRCODE_SUCCESS",
	1:   "ERRCODE_INTERNAL_ERROR",
	2:   "ERRCODE_INVALID_PARAMETER",
	3:   "ERRCODE_ALREADY_EXIST",
	4:   "ERRCODE_NOT_EXIST",
	5:   "ERRCODE_TX_TIMEOUT",
	6:   "ERRCODE_ACCESS_DENIED",
	7:   "ERRCODE_MATH_OVERFLOW",
	20:  "ERRCODE_EXPR_CONDITION_RESULT_FALSE",
	21:  "ERRCODE_EXPR_CONDITION_SYNTAX_ERROR",
	90:  "ERRCODE_INVALID_PUBKEY",
	91:  "ERRCODE_INVALID_PRIKEY",
	92:  "ERRCODE_ASSET_INVALID",
	93:  "ERRCODE_INVALID_SIGNATURE",
	94:  "ERRCODE_INVALID_ADDRESS",
	97:  "ERRCODE_MISSING_OPERATIONS",
	98:  "ERRCODE_TOO_MANY_OPERATIONS",
	99:  "ERRCODE_BAD_SEQUENCE",
	100: "ERRCODE_ACCOUNT_LOW_RESERVE",
	101: "ERRCODE_ACCOUNT_SOURCEDEST_EQUAL",
	102: "ERRCODE_ACCOUNT_DEST_EXIST",
	103: "ERRCODE_ACCOUNT_NOT_EXIST",
	104: "ERRCODE_ACCOUNT_ASSET_LOW_RESERVE",
	105: "ERRCODE_ACCOUNT_ASSET_AMOUNT_TOO_LARGE",
	106: "ERRCODE_ACCOUNT_INIT_LOW_RESERVE",
	111: "ERRCODE_FEE_NOT_ENOUGH",
	112: "ERRCODE_FEE_INVALID",
	114: "ERRCODE_OUT_OF_TXCACHE",
	120: "ERRCODE_WEIGHT_NOT_VALID",
	121: "ERRCODE_THRESHOLD_NOT_VALID",
	144: "ERRCODE_INVALID_DATAVERSION",
	146: "ERRCODE_TX_SIZE_TOO_BIG",
	151: "ERRCODE_CONTRACT_EXECUTE_FAIL",
	152: "ERRCODE_CONTRACT_SYNTAX_ERROR",
	153: "ERRCODE_CONTRACT_TOO_MANY_RECURSION",
	154: "ERRCODE_CONTRACT_TOO_MANY_TRANSACTIONS",
	155: "ERRCODE_CONTRACT_EXECUTE_EXPIRED",
	160: "ERRCODE_TX_INSERT_QUEUE_FAIL",
}
var ERRORCODE_value = map[string]int32{
	"ERRCODE_SUCCESS":                        0,
	"ERRCODE_INTERNAL_ERROR":                 1,
	"ERRCODE_INVALID_PARAMETER":              2,
	"ERRCODE_ALREADY_EXIST":                  3,
	"ERRCODE_NOT_EXIST":                      4,
	"ERRCODE_TX_TIMEOUT":                     5,
	"ERRCODE_ACCESS_DENIED":                  6,
	"ERRCODE_MATH_OVERFLOW":                  7,
	"ERRCODE_EXPR_CONDITION_RESULT_FALSE":    20,
	"ERRCODE_EXPR_CONDITION_SYNTAX_ERROR":    21,
	"ERRCODE_INVALID_PUBKEY":                 90,
	"ERRCODE_INVALID_PRIKEY":                 91,
	"ERRCODE_ASSET_INVALID":                  92,
	"ERRCODE_INVALID_SIGNATURE":              93,
	"ERRCODE_INVALID_ADDRESS":                94,
	"ERRCODE_MISSING_OPERATIONS":             97,
	"ERRCODE_TOO_MANY_OPERATIONS":            98,
	"ERRCODE_BAD_SEQUENCE":                   99,
	"ERRCODE_ACCOUNT_LOW_RESERVE":            100,
	"ERRCODE_ACCOUNT_SOURCEDEST_EQUAL":       101,
	"ERRCODE_ACCOUNT_DEST_EXIST":             102,
	"ERRCODE_ACCOUNT_NOT_EXIST":              103,
	"ERRCODE_ACCOUNT_ASSET_LOW_RESERVE":      104,
	"ERRCODE_ACCOUNT_ASSET_AMOUNT_TOO_LARGE": 105,
	"ERRCODE_ACCOUNT_INIT_LOW_RESERVE":       106,
	"ERRCODE_FEE_NOT_ENOUGH":                 111,
	"ERRCODE_FEE_INVALID":                    112,
	"ERRCODE_OUT_OF_TXCACHE":                 114,
	"ERRCODE_WEIGHT_NOT_VALID":               120,
	"ERRCODE_THRESHOLD_NOT_VALID":            121,
	"ERRCODE_INVALID_DATAVERSION":            144,
	"ERRCODE_TX_SIZE_TOO_BIG":                146,
	"ERRCODE_CONTRACT_EXECUTE_FAIL":          151,
	"ERRCODE_CONTRACT_SYNTAX_ERROR":          152,
	"ERRCODE_CONTRACT_TOO_MANY_RECURSION":    153,
	"ERRCODE_CONTRACT_TOO_MANY_TRANSACTIONS": 154,
	"ERRCODE_CONTRACT_EXECUTE_EXPIRED":       155,
	"ERRCODE_TX_INSERT_QUEUE_FAIL":           160,
}

func (x ERRORCODE) String() string {
	return proto.EnumName(ERRORCODE_name, int32(x))
}
func (ERRORCODE) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_common_db8b929232052d00, []int{0}
}

type KeyPair struct {
	Key                  string   `protobuf:"bytes,1,opt,name=key" json:"key,omitempty"`
	Value                string   `protobuf:"bytes,2,opt,name=value" json:"value,omitempty"`
	Version              int64    `protobuf:"varint,3,opt,name=version" json:"version,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *KeyPair) Reset()         { *m = KeyPair{} }
func (m *KeyPair) String() string { return proto.CompactTextString(m) }
func (*KeyPair) ProtoMessage()    {}
func (*KeyPair) Descriptor() ([]byte, []int) {
	return fileDescriptor_common_db8b929232052d00, []int{0}
}
func (m *KeyPair) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_KeyPair.Unmarshal(m, b)
}
func (m *KeyPair) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_KeyPair.Marshal(b, m, deterministic)
}
func (dst *KeyPair) XXX_Merge(src proto.Message) {
	xxx_messageInfo_KeyPair.Merge(dst, src)
}
func (m *KeyPair) XXX_Size() int {
	return xxx_messageInfo_KeyPair.Size(m)
}
func (m *KeyPair) XXX_DiscardUnknown() {
	xxx_messageInfo_KeyPair.DiscardUnknown(m)
}

var xxx_messageInfo_KeyPair proto.InternalMessageInfo

func (m *KeyPair) GetKey() string {
	if m != nil {
		return m.Key
	}
	return ""
}

func (m *KeyPair) GetValue() string {
	if m != nil {
		return m.Value
	}
	return ""
}

func (m *KeyPair) GetVersion() int64 {
	if m != nil {
		return m.Version
	}
	return 0
}

type Signature struct {
	PublicKey            string   `protobuf:"bytes,1,opt,name=public_key,json=publicKey" json:"public_key,omitempty"`
	SignData             []byte   `protobuf:"bytes,2,opt,name=sign_data,json=signData,proto3" json:"sign_data,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Signature) Reset()         { *m = Signature{} }
func (m *Signature) String() string { return proto.CompactTextString(m) }
func (*Signature) ProtoMessage()    {}
func (*Signature) Descriptor() ([]byte, []int) {
	return fileDescriptor_common_db8b929232052d00, []int{1}
}
func (m *Signature) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Signature.Unmarshal(m, b)
}
func (m *Signature) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Signature.Marshal(b, m, deterministic)
}
func (dst *Signature) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Signature.Merge(dst, src)
}
func (m *Signature) XXX_Size() int {
	return xxx_messageInfo_Signature.Size(m)
}
func (m *Signature) XXX_DiscardUnknown() {
	xxx_messageInfo_Signature.DiscardUnknown(m)
}

var xxx_messageInfo_Signature proto.InternalMessageInfo

func (m *Signature) GetPublicKey() string {
	if m != nil {
		return m.PublicKey
	}
	return ""
}

func (m *Signature) GetSignData() []byte {
	if m != nil {
		return m.SignData
	}
	return nil
}

type LedgerUpgrade struct {
	NewLedgerVersion     int64    `protobuf:"varint,1,opt,name=new_ledger_version,json=newLedgerVersion" json:"new_ledger_version,omitempty"`
	NewValidator         string   `protobuf:"bytes,2,opt,name=new_validator,json=newValidator" json:"new_validator,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *LedgerUpgrade) Reset()         { *m = LedgerUpgrade{} }
func (m *LedgerUpgrade) String() string { return proto.CompactTextString(m) }
func (*LedgerUpgrade) ProtoMessage()    {}
func (*LedgerUpgrade) Descriptor() ([]byte, []int) {
	return fileDescriptor_common_db8b929232052d00, []int{2}
}
func (m *LedgerUpgrade) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_LedgerUpgrade.Unmarshal(m, b)
}
func (m *LedgerUpgrade) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_LedgerUpgrade.Marshal(b, m, deterministic)
}
func (dst *LedgerUpgrade) XXX_Merge(src proto.Message) {
	xxx_messageInfo_LedgerUpgrade.Merge(dst, src)
}
func (m *LedgerUpgrade) XXX_Size() int {
	return xxx_messageInfo_LedgerUpgrade.Size(m)
}
func (m *LedgerUpgrade) XXX_DiscardUnknown() {
	xxx_messageInfo_LedgerUpgrade.DiscardUnknown(m)
}

var xxx_messageInfo_LedgerUpgrade proto.InternalMessageInfo

func (m *LedgerUpgrade) GetNewLedgerVersion() int64 {
	if m != nil {
		return m.NewLedgerVersion
	}
	return 0
}

func (m *LedgerUpgrade) GetNewValidator() string {
	if m != nil {
		return m.NewValidator
	}
	return ""
}

type WsMessage struct {
	Type                 int64    `protobuf:"varint,1,opt,name=type" json:"type,omitempty"`
	Request              bool     `protobuf:"varint,2,opt,name=request" json:"request,omitempty"`
	Sequence             int64    `protobuf:"varint,3,opt,name=sequence" json:"sequence,omitempty"`
	Data                 []byte   `protobuf:"bytes,4,opt,name=data,proto3" json:"data,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *WsMessage) Reset()         { *m = WsMessage{} }
func (m *WsMessage) String() string { return proto.CompactTextString(m) }
func (*WsMessage) ProtoMessage()    {}
func (*WsMessage) Descriptor() ([]byte, []int) {
	return fileDescriptor_common_db8b929232052d00, []int{3}
}
func (m *WsMessage) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_WsMessage.Unmarshal(m, b)
}
func (m *WsMessage) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_WsMessage.Marshal(b, m, deterministic)
}
func (dst *WsMessage) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WsMessage.Merge(dst, src)
}
func (m *WsMessage) XXX_Size() int {
	return xxx_messageInfo_WsMessage.Size(m)
}
func (m *WsMessage) XXX_DiscardUnknown() {
	xxx_messageInfo_WsMessage.DiscardUnknown(m)
}

var xxx_messageInfo_WsMessage proto.InternalMessageInfo

func (m *WsMessage) GetType() int64 {
	if m != nil {
		return m.Type
	}
	return 0
}

func (m *WsMessage) GetRequest() bool {
	if m != nil {
		return m.Request
	}
	return false
}

func (m *WsMessage) GetSequence() int64 {
	if m != nil {
		return m.Sequence
	}
	return 0
}

func (m *WsMessage) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

// for ping messsage
type Ping struct {
	Nonce                int64    `protobuf:"varint,1,opt,name=nonce" json:"nonce,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Ping) Reset()         { *m = Ping{} }
func (m *Ping) String() string { return proto.CompactTextString(m) }
func (*Ping) ProtoMessage()    {}
func (*Ping) Descriptor() ([]byte, []int) {
	return fileDescriptor_common_db8b929232052d00, []int{4}
}
func (m *Ping) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Ping.Unmarshal(m, b)
}
func (m *Ping) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Ping.Marshal(b, m, deterministic)
}
func (dst *Ping) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Ping.Merge(dst, src)
}
func (m *Ping) XXX_Size() int {
	return xxx_messageInfo_Ping.Size(m)
}
func (m *Ping) XXX_DiscardUnknown() {
	xxx_messageInfo_Ping.DiscardUnknown(m)
}

var xxx_messageInfo_Ping proto.InternalMessageInfo

func (m *Ping) GetNonce() int64 {
	if m != nil {
		return m.Nonce
	}
	return 0
}

// for pong message
type Pong struct {
	Nonce                int64    `protobuf:"varint,1,opt,name=nonce" json:"nonce,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Pong) Reset()         { *m = Pong{} }
func (m *Pong) String() string { return proto.CompactTextString(m) }
func (*Pong) ProtoMessage()    {}
func (*Pong) Descriptor() ([]byte, []int) {
	return fileDescriptor_common_db8b929232052d00, []int{5}
}
func (m *Pong) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Pong.Unmarshal(m, b)
}
func (m *Pong) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Pong.Marshal(b, m, deterministic)
}
func (dst *Pong) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Pong.Merge(dst, src)
}
func (m *Pong) XXX_Size() int {
	return xxx_messageInfo_Pong.Size(m)
}
func (m *Pong) XXX_DiscardUnknown() {
	xxx_messageInfo_Pong.DiscardUnknown(m)
}

var xxx_messageInfo_Pong proto.InternalMessageInfo

func (m *Pong) GetNonce() int64 {
	if m != nil {
		return m.Nonce
	}
	return 0
}

func init() {
	proto.RegisterType((*KeyPair)(nil), "protocol.KeyPair")
	proto.RegisterType((*Signature)(nil), "protocol.Signature")
	proto.RegisterType((*LedgerUpgrade)(nil), "protocol.LedgerUpgrade")
	proto.RegisterType((*WsMessage)(nil), "protocol.WsMessage")
	proto.RegisterType((*Ping)(nil), "protocol.Ping")
	proto.RegisterType((*Pong)(nil), "protocol.Pong")
	proto.RegisterEnum("protocol.ERRORCODE", ERRORCODE_name, ERRORCODE_value)
}

func init() { proto.RegisterFile("common.proto", fileDescriptor_common_db8b929232052d00) }

var fileDescriptor_common_db8b929232052d00 = []byte{
	// 874 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x7c, 0x55, 0x6d, 0x73, 0xda, 0x46,
	0x10, 0xae, 0x62, 0x27, 0x36, 0x37, 0xce, 0xf4, 0x7a, 0xb1, 0x13, 0xe2, 0x97, 0xd6, 0x21, 0x4d,
	0xeb, 0x49, 0x3b, 0xfe, 0xd2, 0x5f, 0x70, 0x96, 0xd6, 0x70, 0x63, 0xa1, 0xc3, 0x77, 0x27, 0x8c,
	0xd3, 0x97, 0x1b, 0x01, 0x17, 0xaa, 0x06, 0x4b, 0x54, 0x80, 0x1d, 0xfe, 0x45, 0xa7, 0x5f, 0xfa,
	0xf6, 0xa5, 0xff, 0xa8, 0x7f, 0xa9, 0x23, 0x09, 0x81, 0x70, 0x68, 0x3f, 0xb1, 0xbb, 0xcf, 0xb3,
	0x7b, 0xfb, 0xec, 0x2e, 0x23, 0xb4, 0xd3, 0x8b, 0x6f, 0x6e, 0xe2, 0xe8, 0x74, 0x94, 0xc4, 0x93,
	0x98, 0x6c, 0x67, 0x3f, 0xbd, 0x78, 0x58, 0xbb, 0x40, 0x5b, 0x17, 0x66, 0xd6, 0x0a, 0xc2, 0x84,
	0x60, 0xb4, 0xf1, 0xce, 0xcc, 0xaa, 0xd6, 0xb1, 0x75, 0x52, 0x11, 0xa9, 0x49, 0x76, 0xd1, 0xc3,
	0xdb, 0x60, 0x38, 0x35, 0xd5, 0x07, 0x59, 0x2c, 0x77, 0x48, 0x15, 0x6d, 0xdd, 0x9a, 0x64, 0x1c,
	0xc6, 0x51, 0x75, 0xe3, 0xd8, 0x3a, 0xd9, 0x10, 0x85, 0x5b, 0xab, 0xa3, 0x8a, 0x0c, 0x07, 0x51,
	0x30, 0x99, 0x26, 0x86, 0x1c, 0x21, 0x34, 0x9a, 0x76, 0x87, 0x61, 0x4f, 0x2f, 0xab, 0x56, 0xf2,
	0xc8, 0x85, 0x99, 0x91, 0x03, 0x54, 0x19, 0x87, 0x83, 0x48, 0xf7, 0x83, 0x49, 0x90, 0xd5, 0xdf,
	0x11, 0xdb, 0x69, 0xc0, 0x09, 0x26, 0x41, 0xad, 0x8b, 0x1e, 0xbb, 0xa6, 0x3f, 0x30, 0x89, 0x3f,
	0x1a, 0x24, 0x41, 0xdf, 0x90, 0xaf, 0x11, 0x89, 0xcc, 0x9d, 0x1e, 0x66, 0x41, 0x5d, 0x3c, 0x6f,
	0x65, 0xcf, 0xe3, 0xc8, 0xdc, 0xe5, 0xec, 0x76, 0x1e, 0x27, 0x2f, 0xd1, 0xe3, 0x94, 0x7d, 0x1b,
	0x0c, 0xc3, 0x7e, 0x30, 0x89, 0x93, 0x79, 0xff, 0x3b, 0x91, 0xb9, 0x6b, 0x17, 0xb1, 0x5a, 0x88,
	0x2a, 0x57, 0xe3, 0xa6, 0x19, 0x8f, 0x83, 0x81, 0x21, 0x04, 0x6d, 0x4e, 0x66, 0x23, 0x33, 0xaf,
	0x98, 0xd9, 0xa9, 0xce, 0xc4, 0xfc, 0x3c, 0x35, 0xe3, 0x49, 0x96, 0xbf, 0x2d, 0x0a, 0x97, 0xec,
	0xa3, 0xed, 0x71, 0x6a, 0x46, 0x3d, 0x33, 0x1f, 0xc1, 0xc2, 0x4f, 0x2b, 0x65, 0x92, 0x36, 0x33,
	0x49, 0x99, 0x5d, 0x3b, 0x44, 0x9b, 0xad, 0x30, 0x1a, 0xa4, 0xf3, 0x8c, 0xe2, 0x34, 0x29, 0x7f,
	0x26, 0x77, 0x32, 0x34, 0xfe, 0x2f, 0xf4, 0xf5, 0x3f, 0x15, 0x54, 0x01, 0x21, 0xb8, 0xb0, 0xb9,
	0x03, 0xe4, 0x09, 0xfa, 0x18, 0x44, 0x66, 0x6a, 0xe9, 0xdb, 0x36, 0x48, 0x89, 0x3f, 0x22, 0xfb,
	0xe8, 0x69, 0x11, 0x64, 0x9e, 0x02, 0xe1, 0x51, 0x57, 0x67, 0x29, 0xd8, 0x22, 0x47, 0xe8, 0xf9,
	0x12, 0x6b, 0x53, 0x97, 0x39, 0xba, 0x45, 0x05, 0x6d, 0x82, 0x02, 0x81, 0x1f, 0x90, 0xe7, 0x68,
	0xaf, 0x80, 0xa9, 0x2b, 0x80, 0x3a, 0xd7, 0x1a, 0x3a, 0x4c, 0x2a, 0xbc, 0x41, 0xf6, 0xd0, 0x27,
	0x05, 0xe4, 0x71, 0x35, 0x0f, 0x6f, 0x92, 0xa7, 0x88, 0x14, 0x61, 0xd5, 0xd1, 0x8a, 0x35, 0x81,
	0xfb, 0x0a, 0x3f, 0x5c, 0xa9, 0x94, 0x35, 0xa6, 0x1d, 0xf0, 0x18, 0x38, 0xf8, 0x51, 0x19, 0x6a,
	0x52, 0xd5, 0xd0, 0xbc, 0x0d, 0xe2, 0xdc, 0xe5, 0x57, 0x78, 0x8b, 0x7c, 0x89, 0x5e, 0x16, 0x10,
	0x74, 0x5a, 0x42, 0xdb, 0xdc, 0x73, 0x98, 0x62, 0xdc, 0xd3, 0x02, 0xa4, 0xef, 0x2a, 0x7d, 0x4e,
	0x5d, 0x09, 0x78, 0xf7, 0x7f, 0x88, 0xf2, 0xda, 0x53, 0xb4, 0x33, 0x17, 0xbc, 0xb7, 0x3a, 0x8c,
	0xb9, 0x60, 0xff, 0xec, 0x02, 0xae, 0xf1, 0x9b, 0xb5, 0x98, 0x60, 0x29, 0xf6, 0xed, 0x4a, 0xff,
	0x52, 0x82, 0x2a, 0x18, 0xf8, 0xbb, 0x75, 0x33, 0x94, 0xac, 0xee, 0x51, 0xe5, 0x0b, 0xc0, 0xdf,
	0x93, 0x03, 0xf4, 0xec, 0x3e, 0x4c, 0x1d, 0x47, 0xa4, 0xbb, 0xf9, 0x81, 0x7c, 0x8a, 0xf6, 0x17,
	0xda, 0x99, 0x94, 0xcc, 0xab, 0x6b, 0xde, 0x02, 0x41, 0xd3, 0xd6, 0x25, 0x0e, 0xc8, 0x67, 0xe8,
	0x60, 0x31, 0x4e, 0xce, 0x75, 0x93, 0x7a, 0xd7, 0x65, 0x42, 0x97, 0x54, 0xd1, 0x6e, 0x41, 0x38,
	0xa3, 0x8e, 0x96, 0x70, 0xe9, 0x83, 0x67, 0x03, 0xee, 0x95, 0x53, 0xa9, 0x6d, 0x73, 0xdf, 0x53,
	0xda, 0xe5, 0x57, 0xe9, 0xe0, 0x40, 0xb4, 0x01, 0xf7, 0xc9, 0xe7, 0xe8, 0xf8, 0x3e, 0x41, 0x72,
	0x5f, 0xd8, 0xe0, 0x80, 0x54, 0x1a, 0x2e, 0x7d, 0xea, 0x62, 0x53, 0xee, 0xb0, 0x60, 0xe5, 0x78,
	0xb6, 0xf0, 0xb7, 0x65, 0xf5, 0x05, 0xbe, 0xbc, 0x87, 0x01, 0x79, 0x85, 0x5e, 0xdc, 0x87, 0xf3,
	0xf9, 0x95, 0x7b, 0xf9, 0x91, 0xbc, 0x46, 0x5f, 0xac, 0xa7, 0xd1, 0x66, 0xe6, 0xa4, 0xe2, 0x5d,
	0x2a, 0xea, 0x80, 0xc3, 0x75, 0x7d, 0x33, 0x8f, 0xad, 0x56, 0xfc, 0xa9, 0xbc, 0xcc, 0x73, 0x98,
	0xdf, 0xa8, 0xc7, 0xfd, 0x7a, 0x03, 0xc7, 0xe4, 0x19, 0x7a, 0x52, 0xc6, 0x8a, 0x55, 0x8e, 0xca,
	0x49, 0xdc, 0x57, 0x9a, 0x9f, 0x6b, 0xd5, 0xb1, 0xa9, 0xdd, 0x00, 0x9c, 0x90, 0x43, 0x54, 0x2d,
	0xb0, 0x2b, 0x60, 0xf5, 0x46, 0xae, 0x33, 0xcf, 0x7c, 0xbf, 0xb2, 0xa8, 0x86, 0x00, 0xd9, 0xe0,
	0xae, 0x53, 0x22, 0xcc, 0xc8, 0xf1, 0x92, 0x50, 0x9c, 0x81, 0x43, 0x15, 0x6d, 0x83, 0x90, 0x8c,
	0x7b, 0xf8, 0x17, 0x8b, 0x1c, 0x2e, 0x0f, 0x45, 0x75, 0xb4, 0x64, 0x6f, 0xf2, 0x9d, 0x9f, 0xb1,
	0x3a, 0xfe, 0xd5, 0x22, 0x35, 0x74, 0x54, 0xa0, 0x36, 0xf7, 0x94, 0xa0, 0x76, 0x3a, 0x64, 0xb0,
	0x7d, 0x05, 0xfa, 0x9c, 0x32, 0x17, 0xff, 0xb6, 0x9e, 0xb3, 0x72, 0xff, 0xbf, 0x5b, 0xe4, 0x64,
	0xf9, 0x4f, 0x59, 0x70, 0x16, 0xa7, 0x25, 0xc0, 0xf6, 0xf3, 0x7e, 0xfe, 0xb0, 0xc8, 0x57, 0xcb,
	0x9d, 0x7c, 0xc8, 0x54, 0x82, 0x7a, 0x92, 0xda, 0xf9, 0x19, 0xfe, 0x69, 0x91, 0x57, 0xcb, 0xa5,
	0x7c, 0xd0, 0x1e, 0x74, 0x5a, 0x4c, 0x80, 0x83, 0xff, 0xb2, 0xc8, 0x0b, 0x74, 0x58, 0xd2, 0xc8,
	0x3c, 0x09, 0x42, 0xe9, 0x4b, 0x1f, 0xfc, 0xb9, 0x88, 0xbf, 0xad, 0xb3, 0x1a, 0x3a, 0x0e, 0xe3,
	0xd3, 0xee, 0xf4, 0x26, 0x3e, 0x1d, 0xf7, 0xdf, 0x9d, 0xf6, 0xe2, 0xc4, 0x9c, 0x9a, 0xf7, 0x13,
	0x13, 0xf5, 0xf3, 0xaf, 0x53, 0x77, 0xfa, 0xb6, 0xfb, 0x28, 0xb3, 0xbe, 0xf9, 0x37, 0x00, 0x00,
	0xff, 0xff, 0x4f, 0x8d, 0xeb, 0xa4, 0xb7, 0x06, 0x00, 0x00,
}
