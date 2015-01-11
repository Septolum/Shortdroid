import android
droid = android.Android()

def input(title, sub):
	"""Returns inputted text or '' if cancelled"""
	droid.dialogGetInput(title, sub)
	if str(droid.dialogGetResponse().result)[13:21] != "positive":
		return ""
	else:
		return str(droid.dialogGetResponse().result)[36:-2]
	droid.dialogDismiss()

def alert(title, text):
	"""Doesn't return anything"""
	droid.dialogCreateAlert(title, text)
	droid.dialogSetNeutralButtonText("Ok")
	droid.dialogShow()
	response = droid.dialogGetResponse().result
	droid.dialogDismiss()

def multi(title, items):
	"""Returns the index of the selection or '' if cancelled"""
	droid.dialogCreateAlert(title)
	droid.dialogSetItems(items)
	droid.dialogShow()
	if droid.dialogGetResponse().result == {u'canceled': True}:
		return ""
	else:
		return int(str(droid.dialogGetResponse().result)[10:-1])
	droid.dialogDismiss()
