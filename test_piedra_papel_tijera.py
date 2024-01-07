import unittest
from unittest.mock import patch
import random

# Importa las funciones que deseas probar
from piedra_papel_tijera import obtener_opcion_usuario, obtener_opcion_computadora, determinar_ganador, imprimir_resultado_ronda

class TestJuego(unittest.TestCase):

    @patch('builtins.input', return_value='piedra')
    def test_obtener_opcion_usuario(self, mock_input):
        self.assertEqual(obtener_opcion_usuario(), 'piedra')

    def test_obtener_opcion_computadora(self):
        opciones_validas = ['piedra', 'papel', 'tijera']
        self.assertIn(obtener_opcion_computadora(), opciones_validas)

    def test_determinar_ganador_empate(self):
        self.assertEqual(determinar_ganador('piedra', 'piedra'), 'Empate')

    def test_determinar_ganador_usuario(self):
        self.assertEqual(determinar_ganador('piedra', 'tijera'), 'Usuario')

    def test_determinar_ganador_computadora(self):
        self.assertEqual(determinar_ganador('piedra', 'papel'), 'Computadora')

    def test_imprimir_resultado_ronda_empate(self):
        with patch('builtins.print') as mock_print:
            imprimir_resultado_ronda('Empate')
            mock_print.assert_called_with("¡Empate! Nadie pierde vidas.")

    def test_imprimir_resultado_ronda_usuario(self):
        with patch('builtins.print') as mock_print:
            imprimir_resultado_ronda('Usuario')
            mock_print.assert_called_with("¡Ganaste esta ronda!")

    def test_imprimir_resultado_ronda_computadora(self):
        with patch('builtins.print') as mock_print:
            imprimir_resultado_ronda('Computadora')
            mock_print.assert_called_with("¡Perdiste esta ronda!")

if __name__ == '__main__':
    unittest.main()
