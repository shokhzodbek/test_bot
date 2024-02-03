from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import lang,bam,sam,kam,knopka,til,raqam,a,b,d,s,z,x,c
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"asalom alaykum, {message.from_user.full_name}!")



@dp.message_handler(text ="Telifonlarni narxlari")
async def cilik3(message: types.Message):
    await message.reply("$ pul bormi",reply_markup=bam)
@dp.message_handler(text="iphone")
async def salo (message: types.Message):
    await message.reply("iphone",reply_markup=knopka)
@dp.message_handler(text="iPhone SE 2016")
@dp.message_handler(text="iPhone SE 2020")
@dp.message_handler(text="iPhone 6")
@dp.message_handler(text="iPhone 6S")
@dp.message_handler(text="iPhone 7")
@dp.message_handler(text="iPhone 7 PLUS")
@dp.message_handler(text="iPhone 8")
@dp.message_handler(text="iPhone X")
@dp.message_handler(text="iPhone XS")
@dp.message_handler(text="iPhone XS Max")
@dp.message_handler(text="iPhone XS Max Dual Sim")
@dp.message_handler(text="iPhone XR")
@dp.message_handler(text="iPhone XR Dual Sim")
@dp.message_handler(text="iPhone 11")
@dp.message_handler(text="iPhone 11 Dual Sim")
@dp.message_handler(text="iPhone 11 Pro")
@dp.message_handler(text="iPhone 11 Pro Dual Sim")
@dp.message_handler(text="iPhone 12 mini")
@dp.message_handler(text="iPhone 12 mini Dual Sim")
@dp.message_handler(text="iPhone 12")
@dp.message_handler(text="iPhone 12 Dual Sim")
@dp.message_handler(text="iPhone 11 Pro Max")
@dp.message_handler(text="iPhone 11 Pro Max Dual Sim ")
@dp.message_handler(text="iPhone 12 Pro")
@dp.message_handler(text="Phone 12 Pro Dual Simi")
@dp.message_handler(text="iPhone 12 Pro Max")
@dp.message_handler(text="iPhone 12 Pro Max Dual Sim")
@dp.message_handler(text="iPhone 13 mini")
@dp.message_handler(text="iPhone 13 mini Dual Sim")
@dp.message_handler(text="iPhone 13")
@dp.message_handler(text="iPhone 13 PRO Dual Sim")
@dp.message_handler(text="iPhone 13 PRO")
@dp.message_handler(text="iPhone 13 PRO  Dual Sim")
@dp.message_handler(text="iPhone 13 PRO Max")
@dp.message_handler(text="iPhone 13 PRO Max Dual Sim")
@dp.message_handler(text="iPhone 14 PRO Max")
@dp.message_handler(text="iPhone 14 PRO  Dual Sim")
@dp.message_handler(text="iPhone 14 PRO")
async def saom (message: types.Message):
    await message.reply("Batariyani tanla",reply_markup=a)
@dp.message_handler(text="90~100%")
@dp.message_handler(text="80~90%")
@dp.message_handler(text="70~80%")
@dp.message_handler(text="60~70%")
@dp.message_handler(text="0~60%")
async def sam (message: types.Message):
    await message.reply("hoxlaganigni bos",reply_markup=b)
@dp.message_handler(text="Ha ✅")
@dp.message_handler(text="Yo'q 🚫")
async def lom (message: types.Message):
    await message.reply("iphone3",reply_markup=d)
@dp.message_handler(text="Rose Gold")
@dp.message_handler(text="Gold")
@dp.message_handler(text="Silver")
@dp.message_handler(text="Space Gray")
async def alom (message: types.Message):
    await message.reply("iphone4",reply_markup=s)
@dp.message_handler(text="64 GB")
@dp.message_handler(text="128 GB")
@dp.message_handler(text="256 GB")
@dp.message_handler(text="256 GB")
async def ssalom (message: types.Message):
    await message.reply("iphone5",reply_markup=z)
@dp.message_handler(text="USA|LL")
@dp.message_handler(text="China|CH")
@dp.message_handler(text="UAE|AB")
@dp.message_handler(text="Korea|KH")
async def salcom (message: types.Message):
    await message.reply("iphone6",reply_markup=x)
@dp.message_handler(text="Yo'q yetmagan! ✅")
@dp.message_handler(text="Ha, shikast yetgan 💥")
async def salsom (message: types.Message):
    await message.reply("iphone7",reply_markup=c) 
@dp.message_handler(text="Ha,sotaman ✅")
@dp.message_handler(text="Yo'q,sotmayman 🚫")
async def sda (message: types.Message):
    await message.reply("oxiriga yetib kelding",reply_markup=lang)
@dp.message_handler(text="Ortga◀️")
async def sda (message: types.Message):
    await message.reply("menu",reply_markup=lang)






@dp.message_handler(text ="Sozlamalar")
async def cilik2(message: types.Message):
    await message.reply("nima kerak",reply_markup=sam)

@dp.message_handler(text ="Tilni o'zgartirish")
async def cilik2(message: types.Message):
    await message.reply("nima kerak",reply_markup=til)

@dp.message_handler(text ="F.I.SH o'gartirish")
async def cilik2(message: types.Message):
    await message.reply("nima kerak",reply_markup=sam)

@dp.message_handler(text ="raqamlarni o'zgartirish")
async def cilik2(message: types.Message):
    await message.reply("nima kerak",reply_markup=raqam)
@dp.message_handler(text="Ortga◀️")
async def sa (message: types.Message):
    await message.reply("menu",reply_markup=lang)





@dp.message_handler(text ="Kanalga elon berish")
async def cilik3(message: types.Message):
    await message.reply("https://t.me/Ucell_Humas_Tekin_Internet",reply_markup=kam)










@dp.message_handler(commands="help")
async def help(message:types.Message):
    await message.answer("Qanday yordam bera olaman")
# til uz
@dp.message_handler(text = "Uzbek")
async def help(message:types.Message):
    await message.answer("Sen uzbek tilini tanlading")

@dp.message_handler(text = "Ruskiy")
async def help(message:types.Message):
    await message.answer("Sen rus tilini tanlading")

@dp.message_handler(text = "English")
async def help(message:types.Message):
    await message.answer("Sen english tilini tanlading")
 
@dp.message_handler(text = "salom")
async def hello(message:types.Message):
    await message.answer("Assalom alaykum")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
