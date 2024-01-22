using UnityEngine;
using System.Collections;
using UnityEditor;
using System.Text;
using UnityEngine.SceneManagement;

[AddComponentMenu("MyGame/GameManager")]
public class GameManager : MonoBehaviour {

    public static GameManager Instance;

    //得分
    public int m_score;
    public int m_needscore;
    public int m_bosslife = 0;
    public int m_thisLevelNumber;
    public string m_nextLevel;
    protected bool stop = false;
    public bool Stop
    {
        get { return stop; }
    }
    public delegate void makingHPorReturn(int item, int HPorReturn);
    public event makingHPorReturn MakeHPorReturn;
    //紀錄
    public static int m_hiscore = 0;

    public uint magic;
    private string code = "🛰🛨🚝😁🛳🛨🚌🚕🛋🛤🚚🜮🜬🜧🜦🛳🛨🚌🛼🚰🛻🜚🜯🚷🚃😐🛳🛨🚌🚧🜺😍😯😚🚟🜧🛬🛳🛨🚌🛰🛒😀😜🜝😧🜉🜞🛳🛨🚌😔😷🛝🜯🛻🛳🙉🜱🛳🛨🚌🚷😉🚘🜮🚬🚚🚕🜑🛳🛨🚌🜖🙈🜕🛟😵🜖🛷🛬🛳🛨🚟🛥😜🚞🛡🜿🚞🛼🜘🜖😼🜢🛦🚜🛡🜿🛨🚟🛥😜🚞🜧🚞🛼🜪🜖😼🜊🜖🚜🜧🛨🚟🛥😜🚞🛡🜩🚞🛼🜢🜖😼🜢🜜🚜🛡🜩🛨🚟🛥😜🚞🛡🜲🚞🛼🜒🜖😼🜢😟🚜🛡🜲🛨🚟🛥😜🚞🛡🜣🚞🛼🜮🜖😼🜢😝🚜🛡🜣🛨🚟🛥😜🚞🛡🜋🚞🛼🜵🜖😼🜊😟🚜🛡🜋🛨🚟🛥😜🚞🛡🜾🚞🛼🜹🜖😼🜊🙉🚜🛡🜾🛨🚟🛥😜🚞🛡🜏🚞🛼🜒🜖😼🜢🜭🚜🛡🜏🛨🚟🛥😜🚞🛡🜧🚞🛼🜘🜖😼🜢🛍🚜🛡🜧🛨🚟🛥😜🚞🛡🜄🚞🛼🜩🜖😼🜢😖🚜🛡🜄🛨🚟🛥😜🚞🛡🜒🚞🛼🜆🜖😼🜢🚭🚜🛡🜒🛨🚟🛥😜🚞🛡🜇🚞🛼🜩🜖😼🜢🙂🚜🛡🜇🛨🚟🛥😜🚞🛡🜑🚞🛼🝀🜖😼🜊😠🚜🛡🜑🛨🚟🛥😜🚞🛡🜰🚞🛼🜌🜖😼🜊😔🚜🛡🜰🛨🚟🛥😜🚞🛡🜱🚞🛼🜔🜖😼🜊🝀🚜🛡🜱🛨🚟🛥😜🚞🛡🜓🚞🛼🜂🜖😼🜊🜰🚜🛡🜓🛨🚟🛥😜🚞🛡🜉🚞🛼🜙🜖😼🜊🙀🚜🛡🜉🛨🚟🛥😜🚞🛡🜴🚞🛼🜸🜖😼🜢🚾🚜🛡🜴🛨🚟🛥😜🚞🛡🜊🚞🛼🜣🜖😼🜊😘🚜🛡🜊🛨🚟🛥😜🚞🛡🜸🚞🛼🜎🜖😼🜊🜓🚜🛡🜸🛨🚟🛥😜🚞🛡🜶🚞🛼🜘🜖😼🜊🚳🚜🛡🜶🛨🚟🛥😜🚞🛡🜤🚞🛼🜿🜖😼🜢🜋🚜🛡🜤🛨🚟🛥😜🚞🛡🜻🚞🛼🜌🜖😼🜢🛗🚜🛡🜻🛨🚟🛥😜🚞🛡🜖🚞🛼🜨🜖😼🜢🛁🚜🛡🜖🛨🚟🛥😜🚞🛡🜬🚞🛼🜲🜖😼🜢🛝🚜🛡🜬🛨🚟🛥😜🚞🛡🜫🚞🛼🜱🜖😼🜢🜏🚜🛡🜫🛨🚟🛥😜🚞🛡🜹🚞🛼🜘🜖😼🜊🛥🚜🛡🜹🛨🚟🛥😜🚞🛡🜺🚞🛼🜹🜖😼🜢😿🚜🛡🜺🛨🚟🛥😜🚞🛡🝀🚞🛼🜮🜖😼🜊🜏🚜🛡🝀🛨🚟🛥😜🚞🛡🜽🚞🛼🜨🜖😼🜊😖🚜🛡🜽🛨🚟🛥😜🚞🛡🝁🚞🛼🜥🜖😼🜊🜮🚜🛡🝁🛨🚟🛥😜🚞🛡🜗🚞🛼🜻🜖😼🜊🜐🚜🛡🜗🛨🚟🛥😜🚞🛡🜌🚞🛼🜻🜖😼🜢🜑🚜🛡🜌🛨🚟🛥😜🚞🛡🜎🚞🛼🜋🜖😼🜢🜊🚜🛡🜎🛨🚟🛥😜🚞🛡🜭🚞🛼🜣🜖😼🜢🜃🚜🛡🜭🛨🚟🛥😜🚞🛡🜈🚞🛼🜼🜖😼🜢😁🚜🛡🜈🛨🚟🛥😜🚞🛡🜮🚞🛼🜍🜖😼🜊😛🚜🛡🜮🛨🚟🛥😜🚞🛡🜨🚞🛼🜂🜖😼🜢🜆🚜🛡🜨🛨🚟🛥😜🚞🛡🜯🚞🛼🜲🜖😼🜊🚔🚜🛡🜯🛨🚟🛥😜🚞🛡🜅🚞🛼🜳🜖😼🜊🙈🚜🛡🜅🛨🚟🛥😜🚞🛡🜙🚞🛼🜓🜖😼🜢🛳🚜🛡🜙🛨🚟🛥😜🚞🛡🜢🚞🛼🜷🜖😼🜢🙀🚜🛡🜢🛨🚟🛥😜🚞🛡🜥🚞🛼🜊🜖😼🜢🝀🚜🛡🜥🛨🚟🛥😜🚞🛡🜘🚞🛼🜯🜖😼🜊🛢🚜🛡🜘🛨🚟🛥😜🚞🛡🜪🚞🛼🜩🜖😼🜢🜃🚜🛡🜪🛨🚟🛥😜🚞🛡🜼🚞🛼🜂🜖😼🜢😁🚜🛡🜼🛨🚟🛥😜🚞🛡🜷🚞🛼🜆🜖😼🜊🜋🚜🛡🜷🛨🚟🛥😜🚞🛡🜵🚞🛼🜩🜖😼🜊🚿🚜🛡🜵🛨🚟🛥😜🚞🛡🜐🚞🛼🜴🜖😼🜊🙅🚜🛡🜐🛨🚟🛥😜🚞🛡🜃🚞🛼🝀🜖😼🜊🛤🚜🛡🜃🛨🚟🛥😜🚞🛡🜂🚞🛼🜬🜖😼🜢🜏🚜🛡🜂🛨🚟🛥😜🚞🛡🜳🚞🛼🜫🜖😼🜊🚕🚜🛡🜳🛨🚟🛥😜🚞🛡🜔🚞🛼🜸🜖😼🜢😭🚜🛡🜔🛨🚟🛥😜🚞🛡🜆🚞🛼🜷🜖😼🜢🜥🚜🛡🜆🛨🚟🛥😜🚞🛡🜍🚞🛼🜿🜖😼🜊🛰🚜🛡🜍🛨🚟🛝😜🛨🜗😿🚞🜪🜾🜠🜪🜺🛁🜷🛨🚗😧🜧🛨🚗😟🜕🛍😊🚌🜧🜦🜦🜦😏🜩🛨🜗😤🛨🚝😈🛸😧";
    private string supercode = "";
    public static bool supermode = false;

    //主角
    protected gun m_gun;
    protected int retran;
    public int Retran
    {
        set { retran = value; }
        get { return retran; }
    }
    protected float m_timer;

    void Awake()
    {
        Instance = this;
    }

	// Use this for initialization
	void Start () {
        Time.timeScale = 1;
        for (int i = 6; m_timer < i; ) { m_timer = Random.value * 15; }
        m_score = change.NewScore;
        if (change.Hiscores[m_thisLevelNumber - 1] == 0)
        {
            change.Hiscores[m_thisLevelNumber - 1] = m_score;
        }
        m_hiscore = change.Hiscores[m_thisLevelNumber - 1];
        // 取得主角
        GameObject obj = GameObject.FindGameObjectWithTag("Player");
        if (obj != null)
        {
            m_gun = obj.GetComponent<gun>();
        }
        retran = change.GetRetarn();
	}
	
	// Update is called once per frame
	void Update () {

        m_timer -= Time.deltaTime;
        // 暫停遊戲
        if (Time.timeScale > 0 && Input.GetKeyDown(KeyCode.Escape))
        {
            Time.timeScale = 0;
        }
        if (m_score >= m_needscore)
        {
            stop = true;
        }
        if (m_timer <= 0)
        {
            MakeHPorReturn(Random.Range(0, 13), Random.Range(0, 2));
            for (int i = 6; m_timer < i; ) { m_timer = Random.value * 15; }
        }
        foreach (char enter in Input.inputString)
        {
            supercode += enter.ToString();
            supercode = supercode.Trim(' ', '\r', '\n', '\t');
            if (supercode.Length == 55)
            {
                byte[] mem = new byte[1024];
                Encoding.ASCII.GetBytes(supercode).CopyTo(mem, mem.Length - supercode.Length);
                ulong sp = (ulong)(mem.Length - supercode.Length), bp = (ulong)mem.Length, a = (ulong)(mem.Length - supercode.Length), b = 0, c = 0, d = 0, si = 0, di = 0;
                Transfer.exec(Transfer.etob(code, magic), mem, ref sp, ref bp, ref a, ref b, ref c, ref d, ref si, ref di);
                if (System.Convert.ToBoolean(a))
                    supermode = true;
            }
        }
        if (supercode.Length >= 55)
        {
            supercode = "";
        }
    }

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
        int life = 0;
        if (m_gun != null)
        {
            // 獲得主角的生命值
            life = (int)m_gun.m_life;
            // 遊戲暫停
            if (Time.timeScale == 0)
            {
                // 繼續遊戲按鈕
                if (GUI.Button(new Rect(Screen.width * 0.5f - 50, Screen.height * 0.4f, 100, 30), "繼續遊戲"))
                {
                    Time.timeScale = 1;
                }

                // 退出遊戲按鈕
                if (GUI.Button(new Rect(Screen.width * 0.5f - 50, Screen.height * 0.6f, 100, 30), "退出遊戲"))
                {
                    // 退出遊戲
                    Application.Quit();
                }
            }

        }
        else // game over
        {
            Time.timeScale = 0;
            // 放大字體
            GUI.skin.label.fontSize = 50;

            // 顯示遊戲失敗
            GUI.skin.label.alignment = TextAnchor.LowerCenter;
            GUI.Label(new Rect(0, Screen.height * 0.2f, Screen.width, 60), "遊戲失敗");

            GUI.skin.label.fontSize = 20;
            GUI.Label(new Rect(Screen.width * 0.5f - 420, Screen.height * 0.5f - 30, Screen.width, 30), "你有" + retran + "次重新的機會");

            if (retran > 0)
            {
                // 顯示按鈕
                if (GUI.Button(new Rect(Screen.width * 0.5f - 50, Screen.height * 0.5f, 100, 30), "再試一次"))
                {
                    change.SetRetarn(retran - 1);
                    change.Life = 5;
                    change.Hiscores[m_thisLevelNumber - 1] = m_hiscore;
                    // 讀取目前關卡
                    SceneManager.LoadScene(SceneManager.GetActiveScene().name);
                }
            }
            else
            {
                if (GUI.Button(new Rect(Screen.width * 0.5f - 50, Screen.height * 0.5f, 100, 30), "重新遊戲"))
                {
                    change.SetRetarn(5);
                    change.NewScore = 0;
                    change.Life = 5;
                    change.Hiscores[m_thisLevelNumber - 1] = m_hiscore;
                    // 讀取目前關卡
                    SceneManager.LoadScene("level1");
                }
            }
        }
        if (stop)
        {
            if (m_bosslife <= 0)
            {
                if (m_score > m_needscore + 5)
                {
                    m_score = m_needscore + 5;
                    m_hiscore = m_score;
                    change.NewScore = m_score;
                }
                change.Hiscores[m_thisLevelNumber - 1] = m_hiscore;
                GUI.skin.label.fontSize = 50;

                GUI.skin.label.alignment = TextAnchor.LowerCenter;
                GUI.Label(new Rect(0, Screen.height * 0.2f, Screen.width, 60), "遊戲過關");

                GUI.skin.label.fontSize = 20;
                GUI.Label(new Rect(Screen.width * 0.5f - 420, Screen.height * 0.5f - 30, Screen.width, 30), "你的分數是：" + m_score);
                if(m_nextLevel != "over")
                {
                    // 顯示按鈕
                    if (GUI.Button(new Rect(Screen.width * 0.5f - 50, Screen.height * 0.5f, 100, 30), "下一關"))
                    {
                        change.SetRetarn(retran);
                        // 讀取目前關卡
                        SceneManager.LoadScene(m_nextLevel);
                    }
                }
            }
        }

        GUI.skin.label.fontSize = 15;

        // 顯示主角生命
        GUI.Label(new Rect(5, 5, 100, 30), "生命 " + life);
        GUI.Label(new Rect(5, 25, 100, 30), "重新次數 " + retran);

        // 顯示最高分
        GUI.skin.label.alignment = TextAnchor.LowerCenter;
        GUI.Label(new Rect(0, 5, Screen.width, 30), "關卡" + m_thisLevelNumber);
        GUI.Label(new Rect(0, 25, Screen.width, 30), "最高分" + m_hiscore);

        // 顯示目前得分
        GUI.Label(new Rect(0, 65, Screen.width, 30), "得分 " + m_score);
        if (!stop)
        {
            GUI.Label(new Rect(0, 45, Screen.width, 30), "目標分數 " + m_needscore);
        }
        else
        {
            GUI.Label(new Rect(0, 45, Screen.width, 30), "魔王生命 " + m_bosslife);
        }
      
    }

    void MobileInput()
    {
        int life = 0;
        if (m_gun != null)
        {
            // 獲得主角的生命值
            life = (int)m_gun.m_life;
            // 遊戲暫停
            if (Time.timeScale == 0)
            {
                // 繼續遊戲按鈕
                if (GUI.Button(new Rect(Screen.width * 0.5f - 100, Screen.height * 0.4f, 200, 60), "繼續遊戲"))
                {
                    Time.timeScale = 1;
                }

                // 退出遊戲按鈕
                if (GUI.Button(new Rect(Screen.width * 0.5f - 100, Screen.height * 0.6f, 200, 60), "退出遊戲"))
                {
                    // 退出遊戲
                    Application.Quit();
                }
            }

        }
        else // game over
        {
            Time.timeScale = 0;
            // 放大字體
            GUI.skin.label.fontSize = 100;

            // 顯示遊戲失敗
            GUI.skin.label.alignment = TextAnchor.LowerCenter;
            GUI.Label(new Rect(0, Screen.height * 0.2f, Screen.width, 60), "遊戲失敗");

            GUI.skin.label.fontSize = 40;
            GUI.Label(new Rect(Screen.width * 0.5f - 420, Screen.height * 0.5f - 30, Screen.width, 30), "你有" + retran + "次重新的機會");

            if (retran > 0)
            {
                // 顯示按鈕
                if (GUI.Button(new Rect(Screen.width * 0.5f - 100, Screen.height * 0.5f, 200, 60), "再試一次"))
                {
                    change.SetRetarn(retran - 1);
                    change.Life = 5;
                    change.Hiscores[m_thisLevelNumber - 1] = m_hiscore;
                    // 讀取目前關卡
                    SceneManager.LoadScene(SceneManager.GetActiveScene().name);
                }
            }
            else
            {
                if (GUI.Button(new Rect(Screen.width * 0.5f - 100, Screen.height * 0.5f, 200, 60), "重新遊戲"))
                {
                    change.SetRetarn(5);
                    change.NewScore = 0;
                    change.Life = 5;
                    change.Hiscores[m_thisLevelNumber - 1] = m_hiscore;
                    // 讀取目前關卡
                    SceneManager.LoadScene("level1");
                }
            }
        }
        if (stop)
        {
            if (m_bosslife == 0)
            {
                if (m_score > m_needscore + 5)
                {
                    m_score = m_needscore + 5;
                    m_hiscore = m_score;
                    change.NewScore = m_score;
                }
                change.Hiscores[m_thisLevelNumber - 1] = m_hiscore;
                GUI.skin.label.fontSize = 100;

                GUI.skin.label.alignment = TextAnchor.LowerCenter;
                GUI.Label(new Rect(0, Screen.height * 0.2f, Screen.width, 60), "遊戲過關");

                GUI.skin.label.fontSize = 40;
                GUI.Label(new Rect(Screen.width * 0.5f - 420, Screen.height * 0.5f - 30, Screen.width, 30), "你的分數是：" + m_score);
                // 顯示按鈕
                if (GUI.Button(new Rect(Screen.width * 0.5f - 100, Screen.height * 0.5f, 200, 60), "下一關"))
                {
                    change.SetRetarn(retran);
                    // 讀取目前關卡
                    SceneManager.LoadScene(m_nextLevel);
                }
            }
        }

        GUI.skin.label.fontSize = 30;

        // 顯示主角生命
        GUI.Label(new Rect(5, 5, 100, 30), "生命 " + life);
        GUI.Label(new Rect(5, 25, 100, 30), "重新次數 " + retran);

        // 顯示最高分
        GUI.skin.label.alignment = TextAnchor.LowerCenter;
        GUI.Label(new Rect(0, 5, Screen.width, 30), "關卡" + m_thisLevelNumber);
        GUI.Label(new Rect(0, 25, Screen.width, 30), "最高分" + m_hiscore);

        // 顯示目前得分
        GUI.Label(new Rect(0, 65, Screen.width, 30), "得分 " + m_score);
        if (!stop)
        {
            GUI.Label(new Rect(0, 45, Screen.width, 30), "目標分數 " + m_needscore);
        }
        else
        {
            GUI.Label(new Rect(0, 45, Screen.width, 30), "魔王生命 " + m_bosslife);
        }
      
    }

    // 增加分數
    public void AddScore( int point )
    {
        m_score += point;

        // 更新高分紀錄
        if (m_hiscore < m_score)
            m_hiscore = m_score;
    }

    public int Getscore()
    {
        return m_score;
    }
}
