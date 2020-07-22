"""S.O.L.I.D Design.

Chapter 5. OCP.

Demo settings for the ch_5_main program.
"""
from ch_05_dip import BlackjackCardFactory
from ch_04_ocp import DeckBuilder2
from ch_04_ocp import Shuffler

card_factory = BlackjackCardFactory()
deck_builder = DeckBuilder2
shuffler = Shuffler().shuffle
