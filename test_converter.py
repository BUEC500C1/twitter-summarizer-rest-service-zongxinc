import converter

def test_1():
	assert converter.compressVideo(['@iGuessPoems','@UnusualPoems', '@LitWorks', '@Poem4your_sprog'], 20) == 0
def test_2():
	assert converter.compressVideo(['@iGuessPoems','@UnusualPoems'], 5) == 0


