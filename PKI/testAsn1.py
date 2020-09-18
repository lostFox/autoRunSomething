import asn1tools
foo = asn1tools.compile_files('sequence.asn', 'oer')
# encoded = foo.encode('Signature', ('sm2Signature', 0xABCD))
encoded = foo.encode('SignedDataPayload', {'data': 0x08, 'extDataHash': 0x16})

print(encoded)