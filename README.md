                                                                    CS112 - Projects Lab 1
                                                                        February 2022 


1.  Implement  a  library/program  in  a  programming  language  ofyour choosing to load and validate a DFA input file of the format presented in the Appendix.

dfa_parser_engine.py dfa_config_file 

2.  Implement  a  library/program  in  a  programming  language  ofyour choosing to test acceptance of a DFA - loaded from a DFA config file.

dfa_acceptance_engine.py dfa_config_file <word_to_test>



                                                                           Appendix


DFA input file must be of the following format:
#
#comment lines (skip them)
#
Sigma:
  letter1
  letter2
  . . .
End
#
#comment lines (skip them)
#
States:
  state1
  state2
  state3 ,F
  . . .
  stateK ,S
  . . .
End
#
#comment lines (skip them)
#
Transitions:
  stateX ,letterY ,stateZ
  stateX ,letterY ,stateZ
  . . .
End


  Sections can be in any order. By validation we ask to check that transition section has valid states (first and third word) and valid letters (word two), and also test for determinism. Note that states can be succeeded by ”F”, ”S”, both or nothing. ”S” symbol can succeed only one state.
