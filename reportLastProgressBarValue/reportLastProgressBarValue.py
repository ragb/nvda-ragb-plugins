# NVDA global plugin to report last progressbar value change
#
# This file is covered by the same license as NVDA itself.
# copyright (c) 2011 - Rui Batista <ruiandrebatista@gmail.com>

import controlTypes
import globalPluginHandler
import queueHandler
import speech

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self._lastProgressBarValue = None

	def script_reportLastProgressBarValue(self, gesture):
		if self._lastProgressBarValue is not None:
			queueHandler.queueFunction(queueHandler.eventQueue,
			speech.speakMessage, _("%d porcento") % self._lastProgressBarValue)

	def event_valueChange(self, obj, nextHandler):
		if obj.role == controlTypes.ROLE_PROGRESSBAR and obj.value:
			value = obj.value.rstrip("%\x00")
			if value:
				self._lastProgressBarValue = int(value)
		nextHandler()
	script_reportLastProgressBarValue.__doc__=_("Informa o valor actual da barra de progresso activa") #This description in a docstring form will be spoken while input help is enabled
	
	__gestures = {
	"kb:nvda+control+shift+u" : "reportLastProgressBarValue"
	}
