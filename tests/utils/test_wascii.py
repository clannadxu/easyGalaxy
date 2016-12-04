import unittest
import ezgal.utils as utils
import numpy as np
import StringIO

class test_wascii(unittest.TestCase):
	
	def test_integers( self ):
		
		# test outputting integers
		test_array = np.asarray( [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ] )
		answer = '1 2 3 4\n5 6 7 8'
		output_mock = StringIO.StringIO()
		
		utils.wascii( test_array, output_mock, '%d' )
		
		result = output_mock.getvalue()
		output_mock.close()
		
		self.assertEqual( result, answer )
	
	def test_floats_padding_format( self ):
		
		# test outputting floats
		test_array = np.asarray( [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ] ] )
		answer = ' 1.00  2.00  3.00  4.00\n 5.00  6.00  7.00  8.00\n 9.00 10.00 11.00 12.00'
		output_mock = StringIO.StringIO()
		
		utils.wascii( test_array, output_mock, '%5.2f' )
		
		result = output_mock.getvalue()
		output_mock.close()
		
		self.assertEqual( result, answer )
	
	def test_variable_format( self ):
		
		# test passing a format for each column
		test_array = np.asarray( [ [ 1, 2, 3.16, 4 ], [ 5, 6, 7, 8 ] ] )
		answer = '1  2.00 3.2 4.00\n5  6.00 7.0 8.00'
		output_mock = StringIO.StringIO()
		
		utils.wascii( test_array, output_mock, [ '%1d', '%5.2f', '%3.1f', '%4.2f' ] )
		
		result = output_mock.getvalue()
		output_mock.close()
		
		self.assertEqual( result, answer )
	
if __name__ == '__main__':
	unittest.main()