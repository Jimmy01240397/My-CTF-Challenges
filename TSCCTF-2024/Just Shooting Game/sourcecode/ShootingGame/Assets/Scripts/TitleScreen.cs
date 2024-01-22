using UnityEngine;
using System.Collections;

[AddComponentMenu("MyGame/TitleScreen")]
public class TitleScreen : MonoBehaviour
{

    void OnGUI()
    {
#if UNITY_EDITOR || UNITY_STANDALONE
        MouseInput();   // 滑鼠偵測
#elif UNITY_ANDROID
		MobileInput();  // 觸碰偵測
#endif
    }
    void MouseInput()
    {
        // 文字大小
        GUI.skin.label.fontSize = 48;

        // UI中心對齊
        GUI.skin.label.alignment = TextAnchor.LowerCenter;

        // 顯示標題
        GUI.Label(new Rect(0, 30, Screen.width, 100), "打擊能量球");


        // 開始遊戲按鈕
        if (GUI.Button(new Rect(Screen.width * 0.5f - 100, Screen.height * 0.7f, 200, 30), "開始遊戲"))
        {
            // 開始讀取下一關
            Application.LoadLevel("level1");
        }
    }
    void MobileInput()
    {
        // 文字大小
        GUI.skin.label.fontSize = 96;

        // UI中心對齊
        GUI.skin.label.alignment = TextAnchor.LowerCenter;

        // 顯示標題
        GUI.Label(new Rect(0, 60, Screen.width, 100), "打擊能量球");


        // 開始遊戲按鈕
        if (GUI.Button(new Rect(Screen.width * 0.5f - 200, Screen.height * 0.7f, 400, 60), "開始遊戲"))
        {
            // 開始讀取下一關
            Application.LoadLevel("level1");
        }
    }
}
