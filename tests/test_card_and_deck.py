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
        self.assertEqual(len(d.character_deck), 6)
        self.assertTrue(all(isinstance(card, CharacterCard) for card in d.character_deck))
        
        self.assertEqual(len(d.location_deck), 9)
        self.assertTrue(all(isinstance(card, LocationCard) for card in d.location_deck))
        
        self.assertEqual(len(d.weapon_deck), 6)
        self.assertTrue(all(isinstance(card, WeaponCard) for card in d.weapon_deck))

    def test_decks_are_shuffled(self):
        d = Deck()
        original_character_deck = d.character_deck
        original_weapon_deck = d.weapon_deck
        original_location_deck = d.location_deck
        d.shuffleDecks()
        self.assertNotEqual(original_character_deck, d.character_deck)
        self.assertNotEqual(original_weapon_deck, d.weapon_deck)
        self.assertNotEqual(original_location_deck, d.location_deck)

    def test_add_card_to_character_deck(self):
        d = Deck()
        original_character_deck = d.character_deck
        c = CharacterCard("test")
        d.addCardtoCharacterDeck(c)
        new_deck = d.character_deck
        self.assertLess(len(original_character_deck), len(new_deck))
    
    def test_remove_card_from_character_deck(self):
        d = Deck()
        original_character_deck = d.character_deck
        char_card = CharacterCard("test")
        d.character_deck.append(char_card)
        d.removeCardfromCharacterDeck()
        new_character_deck = d.character_deck
        self.assertGreater(len(original_character_deck), len(new_character_deck))


    def test_add_card_to_weapon_deck(self):
        d = Deck()
        original_weapon_deck = d.weapon_deck
        c = WeaponCard("test")
        d.addCardtoWeaponDeck(c)
        new_weapon_deck = d.weapon_deck
        self.assertLess(len(original_weapon_deck), len(new_weapon_deck))

    def test_remove_card_from_weapon_deck(self):
        d = Deck()
        original_weapon_deck = d.weapon_deck
        weapon_card = WeaponCard("test")
        d.weapon_deck.append(weapon_card)
        d.removeCardfromWeaponDeck()
        new_weapon_deck = d.weapon_deck
        self.assertGreater(len(original_weapon_deck), len(new_weapon_deck))
    
    def test_add_card_to_location_deck(self):
        d = Deck()
        original_location_deck = d.location_deck
        c = LocationCard("test")
        d.addCardtoLocationDeck(c)
        new_location_deck = d.location_deck
        self.assertLess(len(original_location_deck), len(new_location_deck))

    def test_remove_card_from_location_deck(self):
        d = Deck()
        original_location_deck = d.location_deck
        loc_card = LocationCard("test")
        d.location_deck.append(loc_card)
        d.removeCardfromLocationDeck()
        new_location_deck = d.location_deck
        self.assertGreater(len(original_location_deck), len(new_location_deck))
    if __name__ == '__main__':
        unittest.main()