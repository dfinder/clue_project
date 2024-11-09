from gamestate.card import Card,WeaponCard,LocationCard,CharacterCard,Deck
import unittest

class TestCard(unittest.TestCase):
    def test_card_gets_value(self):
        c = Card("test")
        self.assertEqual(c.getValue(), "test")
        c1 = WeaponCard("test")
        self.assertEqual(c1.getValue(), "test")
        c2 = CharacterCard("test")
        self.assertEqual(c2.getValue(), "test")
        c3 = LocationCard("test")
        self.assertEqual(c3.getValue(), "test")

class TestDeck(unittest.TestCase):
    def test_deck_gets_made(self):
        d = Deck()
        self.assertEqual(len(d.deck), 21)
        characterCardList = [card for card in d.deck if isinstance(CharacterCard)]
        locationCardList = [card for card in d.deck if isinstance(LocationCard)]
        weaponCardList = [card for card in d.deck if isinstance(WeaponCard)]
        self.assertEqual(len(characterCardList), 6)
        self.assertEqual(len(locationCardList), 9)
        self.assertEqual(len(weaponCardList), 6)

    def test_deck_is_shuffled(self):
        d = Deck()
        original_deck = d.deck()
        d.shuffleDeck()
        shuffled_deck = d.deck()
        self.assertEqual(original_deck, shuffled_deck)

    def test_add_card(self):
        d = Deck()
        original_deck = d.deck()
        c = Card("test")
        d.addCard(c)
        new_deck = d.deck()
        self.assertNotEqual(len(new_deck), len(original_deck)) #avoids dependencies on other tests
        self.assertLess(len(original_deck), len(new_deck))
    
    def test_remove_card(self):
        d = Deck()
        original_deck = d.deck()
        d.removeCard()
        new_deck = d.deck()
        self.assertNotEqual(len(new_deck), len(original_deck)) #avoids dependencies on other tests
        self.assertGreater(len(original_deck), len(new_deck))
    
    if __name__ == '__main__':
        unittest.main()