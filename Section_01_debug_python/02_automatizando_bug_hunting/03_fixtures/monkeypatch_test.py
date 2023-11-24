def my_function():
    return f"Você digitou {input('Digite algo: ')}!"


def test_my_function(monkeypatch):
    # Input recebe um parâmetro que mock_input não usa, por isso o _
    def mock_input(_):
        return "Python"

    # Trocamos a input do sistema pela nossa mock_input
    monkeypatch.setattr("builtins.input", mock_input)
    output = my_function()

    assert output == "Você digitou Python!"
