import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

  def test_join(self):
      s = ['hello', 'world']
      x = ' '.join(s)
      self.assertEqual(x, 'hello world')
      with self.assertRaises(TypeError):
          x.join(2)

  def test_title(self):
      s = 'hello world'
      self.assertEqual(s.title(), 'Hello World')
      with self.assertRaises(TypeError):
          s.title(2)


  def test_isdigit(self):
    #   self.assertTrue('FOO'.isdigit())
      self.assertFalse('Foo'.isdigit())


  def test_append(self):
      s = ['hello', 'world']
      s.append('object')
      self.assertEqual(s, ['hello', 'world', 'object'])
    #   with self.assertRaises(TypeError):
    #       s.append(2)

    
if __name__ == '__main__':
    unittest.main()