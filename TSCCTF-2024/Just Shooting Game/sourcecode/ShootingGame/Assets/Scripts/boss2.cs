using UnityEngine;
using System.Collections;

public class boss2 : MonoBehaviour {

    public Sprite[] m_sprite;
    public string[] m_colors;
    protected float m_time;
    protected int m_choose;
    protected SpriteRenderer m_sprite2;
    protected boss m_boss;
	// Use this for initialization
	void Start () {

        m_boss = this.gameObject.GetComponent<boss>();
        m_sprite2 = (SpriteRenderer)GetComponent("SpriteRenderer");
        m_choose = Random.Range(0, m_boss.GameManager.m_thisLevelNumber + 1);
        m_boss.m_life = m_boss.GameManager.m_score;
	}
	
	// Update is called once per frame
	void Update () {

        m_time -= Time.deltaTime;
        if(m_time <= 0)
        {
            for (int i = m_choose; i == m_choose; m_choose = Random.Range(0, m_boss.GameManager.m_thisLevelNumber + 1)) { }
            m_sprite2.sprite = m_sprite[m_choose];
            m_boss.ColorNumber = m_choose;
            m_boss.m_color = m_colors[m_choose];
            m_time = Random.Range(3, 8);
        }
	}
}
