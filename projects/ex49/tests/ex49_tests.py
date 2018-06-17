from nose.tools import *
from ex49 import lexicon
from ex49 import parser


def test_match(word_list, expected_word_type, expecting):
	#all these take in tuples lists 
	#word_list should be lexicon.break_sentence('princess eat bear')
	#this would return [('noun', 'princess'), ('verb', 'eat'), ('noun', 'bear')]
	result = parser.match(word_list, expecting)
	assert_equal(result, expecting)
	

def test_skip(word_list, word_type, expecting):
	result = parser.skip(word_list, word_type)
	assert_equal(result, expecting)

def test_peek(word_list, expecting):
	result = parser.peek(word_list)
	assert_equal(result, expecting)

def test_parse_subject(word_list, subject, expecting):
	result = parser.parse_subject(word_list, subject)
	assert_equal(result, expecting)

def test_parse_object(word_list, expecting):
	result = parser.parse_object(word_list)
	assert_equal(result, expecting)

def test_parse_verb(word_list, expecting):
	result = parser.parse_verb(word_list)
	assert_equal(result, expecting)

#def test_parse_sentence(word_list, expecting):
	#result = parser.test_parse_sentence(word_list)
	#assert_equal(result, expecting)



def nvo_run_tests():
	nvo = [('noun', 'princess'), ('verb', 'eat'), ('noun', 'bear')]
	test_peek(nvo, 'noun')
	test_match(nvo, 'noun', ('noun', 'princess'))
	#this test skip does not return anything?
	test_skip(nvo, 'noun', None)
	
	test_parse_subject(nvo,('noun', 'princess'), Sentence('princess','eat','bear'))
	test_parse_verb(nvo,('verb', 'eat'))
	test_parse_object(nvo,('noun', 'bear'))
	test_parse_sentence(nvo, Sentence('princess', 'eat', 'bear'),)

	#assert_equal(result, 'noun')
nvo_run_tests()
#def run_tests():
	#test_peek([('noun, bear'),('direction','west')], 'noun')
	#test_peek([], None)
