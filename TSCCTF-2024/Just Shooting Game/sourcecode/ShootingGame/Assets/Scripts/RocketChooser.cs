using UnityEngine;
using System.Collections;

public class RocketChooser : MonoBehaviour {

    public Sprite[] m_sprite;
    protected SpriteRenderer m_sprite2;
    protected Transform m_transform;
    protected gun Gun;
    protected AndroidTouch Gun2;

    // Use this for initialization
    void Awake()
    {
        Gun = this.gameObject.GetComponent<gun>();
        Gun.ChooseRocket += doChooseRocket;
        Gun2 = this.gameObject.GetComponent<AndroidTouch>();
        Gun2.ChooseRocket += doChooseRocket;
        m_sprite2 = (SpriteRenderer)GetComponent("SpriteRenderer");
        m_transform = this.transform;
    }
	void Start () {

	}
	
	// Update is called once per frame
	void Update () {
	

	}
    protected void doChooseRocket(out int i)
    {
        i = 0;
        i = Random.Range(0, m_sprite.Length);
        m_sprite2.sprite = m_sprite[i];
    }
}
