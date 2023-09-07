data = """
{"_id":{"$oid":"5be4584f1d8eb55a0316111b"},"request":true,"name":"Anil Kumar","email":"anil.kr@gmail.com","password":"$2a$10$aF.FVRu9gi45OPElHsugbeWgKDEOaIly2ghlsLUuLpiM2elXw840i","role":"Accountant","isAdmin":false,"created":"November 8, 2018","__v":0,"privileges":{"create":true,"delete":false,"read":true,"update":false}}
{"_id":{"$oid":"5be80de36ed39a374b488115"},"privileges":{"read":true,"create":true,"update":true,"delete":false},"request":true,"name":"Sushil Kumar Besra","email":"sushil@yahoo.com","password":"$2a$10$x9QVBQIshU37ap16vYiuPegtVBSWKtJidgcYSYAgb9OvuZhHLVqv6","role":"Teacher","isAdmin":false,"created":"November 11, 2018","__v":0}
{"_id":{"$oid":"5be8101ee0ff0d35cf2a65e7"},"privileges":{"read":true,"create":true,"update":true,"delete":true},"request":true,"name":"Aarish Rahman","email":"aarish@outlook.com","password":"$2a$10$x9QVBQIshU37ap16vYiuPegtVBSWKtJidgcYSYAgb9OvuZhHLVqv6","role":"Administrator","isAdmin":true,"created":"November 11, 2018","__v":0}
{"_id":{"$oid":"5be8596d684dcf5751e768bb"},"privileges":{"read":true,"create":false,"update":false,"delete":false},"request":true,"name":"Anjum Jawed","email":"anjum@gmail.com","password":"$2a$10$6DDgiCCqT.cdLauyNPdebu6yl.NJBCUviCXA.09wbLewXbejRgh16","role":"Principal","isAdmin":true,"created":"November 11, 2018","__v":0}
{"_id":{"$oid":"5beaf3ebda35e85d498efa00"},"privileges":{"read":true,"create":true,"update":true,"delete":false},"isAdmin":false,"request":true,"name":"Annu Kumari","email":"annu@gmail.com","password":"$2a$10$NCiJZoJ7zkGSHmdmi9LbLOWn9hgyScfVIjo1aS.CMmxoXo96Dpz0u","role":"Teacher","created":"November 13, 2018","__v":0}
{"_id":{"$oid":"5bf579f6702e5d3be4b8e379"},"privileges":{"read":false,"create":false,"update":false,"delete":false},"isAdmin":false,"request":false,"name":"Nikhal Agarwal","email":"nik@gmail.com","password":"$2a$10$LCACebdefWsTM9y7Nsmkd.OwzZpNwBSW8V8zDdhEW/Hr0o5.zkqwG","role":"Principal","created":"November 21, 2018","__v":0}
{"_id":{"$oid":"5bf57a0b702e5d3be4b8e37a"},"privileges":{"read":false,"create":false,"update":false,"delete":false},"isAdmin":false,"request":false,"name":"Nikita Singh","email":"nikita@gmail.com","password":"$2a$10$qg0q3YDWBYe6LPmI6QGtWeZpmSwJD0.WSfa63.XDtIEJbZ8lRhx.m","role":"Teacher","created":"November 21, 2018","__v":0}
{"_id":{"$oid":"5bf57a32702e5d3be4b8e37b"},"privileges":{"read":false,"create":false,"update":false,"delete":false},"isAdmin":false,"request":false,"name":"Mukesh Kumar","email":"mukesh@gmail.com","password":"$2a$10$rwMnOCyLWvKlIlG3sKCYCeGtsMhHYx0JF5ahlXnYrIL49q1TrLFY2","role":"Accountant","created":"November 21, 2018","__v":0}
{"_id":{"$oid":"5bfbb3c08cd424098c0b73ef"},"privileges":{"read":true,"create":true,"update":true,"delete":true},"isAdmin":true,"request":true,"name":"Sahana Afrin","email":"afrin@gmail.com","password":"$2a$10$vK.GZRiVaQezvzMY/l0OIe8pTMgfINVR7LNdP5vK.DQPEsjXHT8oq","role":"Principal","created":"November 26, 2018","__v":0}
{"_id":{"$oid":"5bfe6972a3315212db2b1caf"},"privileges":{"read":true,"create":true,"update":true,"delete":false},"isAdmin":false,"request":true,"name":"Abhijeet Kumar","email":"abhijeet@gmail.com","password":"$2a$10$MnYhWurxYKiLygFLZ58gweSM8IJr92LRMQ3/x.gEgr5QTDqXyUO7i","role":"Teacher","created":"November 28, 2018","__v":0}
{"_id":{"$oid":"5bfed4080f4d5e0cc1af3461"},"privileges":{"read":false,"create":false,"update":false,"delete":false},"isAdmin":false,"request":false,"name":"S.A. Siddique","email":"siddique@gmail.com","password":"$2a$10$gspXILKVhGr44XBbOQhQjehnS254IKjWCVaoBOSNbS/ThHSs0VBEy","role":"Principal","created":"November 28, 2018","__v":0}

"""


# Split the data into individual documents
documents = data.strip().split("\n\n")

# Generate insertOne() commands for each document
for doc in documents:
    print(f'db.users.insertOne({doc});')
