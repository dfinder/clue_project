from gamestate.card import Card,WeaponCard,LocationCard,CharacterCard
def test_card_gets_value():
    c = Card("test")
    assert(c.getValue(), "test")
    c1 = WeaponCard("test")
    assert(c1.getValue(), "test")
    c2 = CharacterCard("test")
    assert(c2.getValue(), "test")
    c3 = LocationCard("test")
    assert(c3.getValue(), "test")

def test_deck_gets_made():
    pass