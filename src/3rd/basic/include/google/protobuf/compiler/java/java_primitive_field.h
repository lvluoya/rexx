
#ifndef GOOGLE_PROTOBUF_COMPILER_JAVA_PRIMITIVE_FIELD_H__
#define GOOGLE_PROTOBUF_COMPILER_JAVA_PRIMITIVE_FIELD_H__

#include <map>
#include <string>
#include <google/protobuf/compiler/java/java_field.h>

namespace google {
namespace protobuf {
  namespace compiler {
    namespace java {
      class Context;           // context.h
      class ClassNameResolver; // name_resolver.h
    }
  }
}

namespace protobuf {
namespace compiler {
namespace java {

class ImmutablePrimitiveFieldGenerator : public ImmutableFieldGenerator {
 public:
  explicit ImmutablePrimitiveFieldGenerator(
      const FieldDescriptor* descriptor, int messageBitIndex,
      int builderBitIndex, Context* context);
  ~ImmutablePrimitiveFieldGenerator();

  // implements ImmutableFieldGenerator ---------------------------------------
  int GetNumBitsForMessage() const;
  int GetNumBitsForBuilder() const;
  void GenerateInterfaceMembers(io::Printer* printer) const;
  void GenerateMembers(io::Printer* printer) const;
  void GenerateBuilderMembers(io::Printer* printer) const;
  void GenerateInitializationCode(io::Printer* printer) const;
  void GenerateBuilderClearCode(io::Printer* printer) const;
  void GenerateMergingCode(io::Printer* printer) const;
  void GenerateBuildingCode(io::Printer* printer) const;
  void GenerateParsingCode(io::Printer* printer) const;
  void GenerateParsingDoneCode(io::Printer* printer) const;
  void GenerateSerializationCode(io::Printer* printer) const;
  void GenerateSerializedSizeCode(io::Printer* printer) const;
  void GenerateFieldBuilderInitializationCode(io::Printer* printer) const;
  void GenerateEqualsCode(io::Printer* printer) const;
  void GenerateHashCode(io::Printer* printer) const;

  string GetBoxedType() const;

 protected:
  const FieldDescriptor* descriptor_;
  map<string, string> variables_;
  const int messageBitIndex_;
  const int builderBitIndex_;
  Context* context_;
  ClassNameResolver* name_resolver_;

 private:
  GOOGLE_DISALLOW_EVIL_CONSTRUCTORS(ImmutablePrimitiveFieldGenerator);
};

class ImmutablePrimitiveOneofFieldGenerator
    : public ImmutablePrimitiveFieldGenerator {
 public:
  ImmutablePrimitiveOneofFieldGenerator(
      const FieldDescriptor* descriptor, int messageBitIndex,
      int builderBitIndex, Context* context);
  ~ImmutablePrimitiveOneofFieldGenerator();

  void GenerateMembers(io::Printer* printer) const;
  void GenerateBuilderMembers(io::Printer* printer) const;
  void GenerateBuildingCode(io::Printer* printer) const;
  void GenerateMergingCode(io::Printer* printer) const;
  void GenerateParsingCode(io::Printer* printer) const;
  void GenerateSerializationCode(io::Printer* printer) const;
  void GenerateSerializedSizeCode(io::Printer* printer) const;

 private:
  GOOGLE_DISALLOW_EVIL_CONSTRUCTORS(ImmutablePrimitiveOneofFieldGenerator);
};

class RepeatedImmutablePrimitiveFieldGenerator
    : public ImmutableFieldGenerator {
 public:
  explicit RepeatedImmutablePrimitiveFieldGenerator(
      const FieldDescriptor* descriptor, int messageBitIndex,
      int builderBitIndex, Context* context);
  virtual ~RepeatedImmutablePrimitiveFieldGenerator();

  // implements ImmutableFieldGenerator ---------------------------------------
  int GetNumBitsForMessage() const;
  int GetNumBitsForBuilder() const;
  void GenerateInterfaceMembers(io::Printer* printer) const;
  void GenerateMembers(io::Printer* printer) const;
  void GenerateBuilderMembers(io::Printer* printer) const;
  void GenerateInitializationCode(io::Printer* printer) const;
  void GenerateBuilderClearCode(io::Printer* printer) const;
  void GenerateMergingCode(io::Printer* printer) const;
  void GenerateBuildingCode(io::Printer* printer) const;
  void GenerateParsingCode(io::Printer* printer) const;
  void GenerateParsingCodeFromPacked(io::Printer* printer) const;
  void GenerateParsingDoneCode(io::Printer* printer) const;
  void GenerateSerializationCode(io::Printer* printer) const;
  void GenerateSerializedSizeCode(io::Printer* printer) const;
  void GenerateFieldBuilderInitializationCode(io::Printer* printer) const;
  void GenerateEqualsCode(io::Printer* printer) const;
  void GenerateHashCode(io::Printer* printer) const;

  string GetBoxedType() const;

 private:
  const FieldDescriptor* descriptor_;
  map<string, string> variables_;
  const int messageBitIndex_;
  const int builderBitIndex_;
  Context* context_;
  ClassNameResolver* name_resolver_;

  GOOGLE_DISALLOW_EVIL_CONSTRUCTORS(RepeatedImmutablePrimitiveFieldGenerator);
};

}  // namespace java
}  // namespace compiler
}  // namespace protobuf

}  // namespace google
#endif  // GOOGLE_PROTOBUF_COMPILER_JAVA_PRIMITIVE_FIELD_H__
