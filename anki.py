import genanki

class anki:

  @classmethod
  def get_field_info(self, df):
    cloze = ''
    en_mean = ''

    word, ipa, vi_mean = self.get_ipa_vi_csv(df)

    len_Word  = len(word)
    if len_Word > 2:
      cloze = word[0] + '.....' + word[len_Word - 1]
    else:
      cloze = word[0] + '.....'

    fields = [
      word,
      cloze,
      ipa,
      '',
      en_mean,
      vi_mean,
      ''
    ]

    return fields

  @classmethod
  def get_ipa_vi_csv(self, row):
    word = row['Word']
    ipa = row['Ipa']
    vi_mean = row['Meaning']
    
    len_vi_mean = len(vi_mean)
    if vi_mean[0] == '"' and vi_mean[len_vi_mean - 1] == '"':
      vi_mean = vi_mean[1, len_vi_mean - 2]
    vi_mean = vi_mean.capitalize()

    return word, ipa, vi_mean

  @classmethod
  def gen_anki_note(self, note_type, df):

    my_model = genanki.Model(
    6666666666,
    note_type,
    fields=[
      {'name': 'Word'},
      {'name': 'Cloze'},
      {'name': 'Phonetic symbol'},
      {'name': 'Audio'},
      {'name': 'English Meaning'},
      {'name': 'Vietnamese Meaning'},
      {'name': 'Picture'}
    ],
    templates=[
      {
        'name': 'Card 1',
        'qfmt': '{{Word}}',
        'afmt': '{{FrontSide}}<hr id="Word">{{Word}}',
      },
    ])
    
    my_note = genanki.Note(
      model = my_model,
      fields= self.get_field_info(df)
    )
    
    return my_note
  
  @classmethod
  def gen_anki_apkg_file(self, deck_name, note_type, df):
    error_words = []

    my_deck = genanki.Deck(
      2059400110,
      deck_name)

    for _, row in df.iterrows():
      try:
        word = row['Word']
        print(f'-------------------{word}-------------------')
        my_note = self.gen_anki_note(note_type, row)
        my_deck.add_note(my_note)
      except:
        error_words.append(word)
    
    genanki.Package(my_deck).write_to_file(f'{deck_name}.apkg')

    return error_words