import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_read_env(self):
        # Arrange
        file_name = 'config'
        file_output = f'{file_name}.env'
        file_content = 'name=${name}'

        # Act
        main.main(file_name)

        # Assert
        with open(file_output) as file:
            content = ''.join(file.readlines())
            self.assertEqual(file_content, content)


if __name__ == '__main__':
    unittest.main()
