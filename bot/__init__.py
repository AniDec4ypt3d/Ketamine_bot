from .database.mongodb import MongoDB
import pymongo
from .core.logger import log
import sys
mdb = MongoDB("mongodb+srv://Ani:s4ZxlUYnolSPaMI3@cluster0.2sfbj.mongodb.net/?retryWrites=true&w=majority',serverSelectionTimeoutMS=5000")
my_client = pymongo.MongoClient('mongodb+srv://Ani:s4ZxlUYnolSPaMI3@cluster0.2sfbj.mongodb.net/?retryWrites=true&w=majority')
sdb = my_client["bot"]

def insert_gates(sdb):
    dict = [
    {"_id": "chk", "status": True, "status_logo": "ON ✅", "gate_type": "auth", "cmd_name": "chk", "gate_name": "𝑺𝒚𝒃𝒍𝒖𝒔", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": False, "date": "2022-05-29","comment": "No comment added"},
    {"_id": "ad", "status": True, "status_logo": "ON ✅", "gate_type": "charge", "charge_amount": "56", "cmd_name": "ad", "gate_name": "Adyen ", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d",         "is_paid": True, "date": "2022-05-29","comment": "No comment added"},
    {"_id": "mass", "status": True, "status_logo": "ON ✅", "gate_type": "mass", "cmd_name": "mass", "gate_name": "Stripe", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True, "date": "2022-05-29","comment": "No comment added"},
    {"_id": "sho", "status": True, "status_logo": "ON ✅", "gate_type": "auth", "charge_amount": "5", "cmd_name": "sho", "gate_name": "Spreedly", "made_by_id": 5640958137, "made_by_name": "𓆩AniDec4ypt3d", "is_paid": True, "date": "2022-05-30","comment": "No comment added"},
    {"_id": "wp", "status": True, "status_logo": "ON ✅", "gate_type": "charge", "charge_amount": "5", "cmd_name": "wp", "gate_name": "Wepay", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True, "date":         "2022-06-01","comment": "No comment added"},
    {"_id": "mchk", "status": True, "status_logo": "ON ✅", "gate_type": "mass", "cmd_name": "mchk", "gate_name": "Stripe Charge $10", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True, "date": "2022-06-19","comment": "No comment added"},
    {"_id": "at", "status": True, "status_logo": "ON ✅", "gate_type": "charge", "charge_amount": "36", "cmd_name": "at", "gate_name": "Adyen", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True, "date": "2022-07-01","comment": "No comment added"},
    {"_id": "al", "status": True, "status_logo": "ON ✅ ", "gate_type": "charge", "charge_amount": "10", "cmd_name": "al", "gate_name": "Authorize", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True, "d        ate": "2022-07-02","comment": "No comment added"},
    {"_id": "cc", "status": True, "status_logo": "ON ✅", "gate_type": "charge", "charge_amount": "1", "cmd_name": "cc", "gate_name": "Stripe 0.", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True, "date": "2022-07-        03","comment": "No comment added"},
    {"_id": "ck", "status": True, "status_logo": "ON ✅", "gate_type": "charge", "charge_amount": "5", "cmd_name": "ck", "gate_name": "Stripe 0.", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True, "date": "2022-07-03"},
    {"_id": "pf", "status": True, "status_logo": "ON ✅", "gate_type": "charge", "charge_amount": "20", "cmd_name": "pf", "gate_name": "Payflow $", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d",         "is_paid": True, "date": "2022-07-03","comment": "No comment added"},
    {"_id": "str", "status": True, "status_logo": "ON ✅", "gate_type": "charge", "charge_amount": "5", "cmd_name": "str", "gate_name": "Stripe", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": True        , "date": "2022-07-03","comment": "No comment added"},
    {"_id": "vbv", "status": True, "status_logo": "ON ✅", "gate_type": "other", "cmd_name": "vbv", "gate_name": "Braintree Vbv Check", "made_by_id": 5640958137, "made_by_name": "AniDec4ypt3d", "is_paid": False, "date": "2022-07-03","comment": "No comment added"}]

    x = sdb["gate"].insert_many(dict)
    return x

# insert_gates(sdb)

try:
    x = sdb.list_collection_names()
    log.info("Mongodb Connected...")
    log.debug("Found {} collections".format('-'.join(x)))
except Exception as er:
    log.exception(er)
    sys.exit(1)


log.info("check if gates are added or not.")



is_added = sdb['gate'].count_documents({})
if not is_added:
    added = insert_gates(sdb)
    log.debug("added gates to database.")



