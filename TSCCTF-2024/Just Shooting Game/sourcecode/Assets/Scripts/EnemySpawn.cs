using UnityEngine;
using System.Collections;

public class EnemySpawn : MonoBehaviour
{
    // 敵人的Prefab
    public Transform[] m_enemy;
    public Transform[] m_HPandReturn;
    public bool m_yesNoStop;
    public bool m_youAreBoss;
    public int m_itemNumber;

    // 產生敵人的時間間隔
    protected float m_timer;

    protected int m_choose;
    protected GameManager m_GameManager;

    protected Transform m_transform;

	// Use this for initialization
	void Start () 
    {
        m_transform = this.transform;
        m_itemNumber = (int)m_transform.position.x + 6;
        m_timer = Random.value * 15.0f;
        m_choose = Random.Range(0, m_enemy.Length);
        GameObject obj = GameObject.FindGameObjectWithTag("GameManager");
        if (obj != null)
        {
            m_GameManager = obj.GetComponent<GameManager>();
        }
        m_GameManager.MakeHPorReturn += doMakeHPorReturn;
	}
	
	// Update is called once per frame
	void Update () 
    {

        if (m_GameManager.Stop == m_yesNoStop)
        {
            if (!m_youAreBoss)
            {
                m_timer -= Time.deltaTime;
                if (m_timer <= 0)
                {
                    m_timer = Random.value * 25.0f;
                    m_choose = Random.Range(0, m_enemy.Length);
                    Instantiate(m_enemy[m_choose], m_transform.position, Quaternion.identity);
                }
            }
            else
            {
                m_choose = 0;
                Instantiate(m_enemy[m_choose], m_transform.position, Quaternion.identity);
                m_yesNoStop = false;
            }
        }
	}

    void  OnDrawGizmos () 
    {
        Gizmos.DrawIcon (transform.position, "item.png", true);
    }
    void doMakeHPorReturn(int a, int b)
    {
        if (m_itemNumber == a)
        {
            if (!m_youAreBoss)
            {
                Instantiate(m_HPandReturn[b], m_transform.position, Quaternion.identity);
            }
        }
    }
}
