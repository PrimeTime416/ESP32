print('**** Imported: classPlay.py')



# ******************************* PLAY ******************************

"""
  https://dev.to/spukas/finite-state-machine-in-javascript-1ki1
  Fork: PrimeTime416: June 12, 2022

  Input:	Current state:	Next state:
  PRESS:	OFF	         :  ON        :
  PRESS:	ON	         :  BLINK     :
  PRESS:	BLINK	       :  OFF       :
"""

class Machine:
  _state = 0x00
  _old_state = None
  def current():
    print('Transition Initalized', self._state)
    
  def ITERATE(self):
    def press(self):
      self.dispatch('press', self._state)
    action = {
      "press": press
    }
    return action

  def QUAD1(self):
    def press(self):
      self._state = "ON"
      self._status()
    action = {
      "press": press
    }
    return action
    
  def QUAD2(self):
    def press(self):
      self._state = "BLINK"
      self._status()
    action = {
      "press": press
    }
    return action
  
  def QUAD3(self):
    def press(self):
      self._state = "OFF"
      self._status()
    action = {
      "press": press
    }
    return action

  def QUAD4(self):
    def press(self):
      self._state = "OFF"
      self._status()
    action = {
      "press": press
    }
    return action

  def __init__(self):
    print('Object: Machine: Constructed')
  
  def dispatch(self, actionX="press", stateName="ITERATE"):
    if stateName in self._transitions:
      stateX = self._transitions[stateName](self)
      self._currentState()
      if actionX in stateX:
        stateX[actionX](self)
      else: print("Invalid ACTION!: {}".format(actionX));
    else:
      print("Invalid STATE!: {}".format(stateName));
  
  def _status(self):
    print("Transitioned froms {} to  {} state.".format(self._old_state, self._state))
  
  def _currentState(self):
    self._old_state = self._state

  _transitions = {
    "current": current,
    "QUAD1": QUAD1,
    "QUAD2": QUAD2,
    "QUAD3": QUAD3,
    "QUAD4": QUAD4,
    "ITERATE": ITERATE
  }



# ******************************* TESTING ******************************
# st1 = Machine()
# print(dir(st1))

# st1.dispatch()
# st1.dispatch()
# st1.dispatch()
# st1.dispatch()


# st1.dispatch('press')
# st1.dispatch('press')
# st1.dispatch('press')
# st1.dispatch('press')

# st1.dispatch('press')
# st1.dispatch('press')
# st1.dispatch('press')
# st1.dispatch('press')

# st1.dispatch("press", "ON")
# st1.dispatch("press", "ON")
# st1.dispatch("press", "BLINK")
# st1.dispatch("press", "BLINK")
# st1.dispatch("press", "OFF")
# st1.dispatch('press', "OFF")