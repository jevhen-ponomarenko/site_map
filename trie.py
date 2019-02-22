import pygtrie as trie

t = trie.StringTrie()
t['eshop/pece-a-laska'] = True
t['eshop/pece-a-laska/telo'] = True
t['eshop/pece-a-laska/mleko'] = True
t['eshop/pece-a-laska/telo/sila'] = True

print(t.has_subtrie('eshop'))
print(list(t['eshop/pece-a-laska/telo' :]))