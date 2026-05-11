using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class UIManager : MonoBehaviour
{
    [Header("UI Elements")]
    public TMP_InputField chatInputField;
    public Button sendButton;
    public Transform chatDisplay;
    public TMP_Dropdown modelDropdown;

    private void Start()
    {
        sendButton.onClick.AddListener(SendMessage);
        PopulateModelDropdown();
    }

    private void SendMessage()
    {
        string message = chatInputField.text;
        if (!string.IsNullOrWhiteSpace(message))
        {
            DisplayMessage(message);
            chatInputField.text = string.Empty;
        }
    }

    private void DisplayMessage(string message)
    {
        GameObject chatMessage = new GameObject("ChatMessage");
        TextMeshProUGUI textMeshPro = chatMessage.AddComponent<TextMeshProUGUI>();
        textMeshPro.text = message;
        chatMessage.transform.SetParent(chatDisplay);
    }

    private void PopulateModelDropdown()
    {
        modelDropdown.ClearOptions();
        List<string> models = new List<string>() { "Model A", "Model B", "Model C" };
        modelDropdown.AddOptions(models);
    }
}