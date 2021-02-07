#include "stdafx.h"
#include "PressPlateO.h"

PressPlateO::PressPlateO(void)
	: CQuestInfoSuper()
{
	m_nTargetNpcId = 10012;

	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(O�� ���� ���� ������. ��ȣ 1�� �����ϴ� �� ����.)"));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00000001;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00000011;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(O ���ڰ� ���� ������ ���� ����.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "���� ��-��."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "��-���� ������Ʈ�� �Ķ���� ������ �����ϰڴ�."));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "�غ� �Ǿ��ٸ� ������ ��ȣ�� ���. ��-��."));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00000111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00001111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�Ƿ� ����� ���ؼ��� �ؾ� �Ѵٰ� �����ߴ�.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[���� : ��ȣ.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[��� : 1�� ���� ������ TOP 30�� ������ �ش�.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "�� ���� �Ķ� �÷��ǵ�ũ�� �־��. ��-��."));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b00011111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b00111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�翬�� �� �켱�Ѵٰ� �����ߴ�.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[���� : ���� �ʿ�.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[��� : ������ ��å�� �켱�Ѵ�.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[���� : ���� �Ϸ�.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "�� ���� ��� CD�� �־��. ��-��."));
	{
		ST_QUEST_FLAG_FILTER Condition;
		Condition.mask[7] = 0xFF;
		Condition.flags[7] = 0b01111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_CONDITION, Condition));
	}
	m_Sequence.push_back(ST_QUEST_SEQUENCE(0, "(�翬�� �� �� �����Ŷ� �����ߴ�.)"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[���� : ��ȣ.]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[��� : https://quickconnect.to/bobtop]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "[��� : ID: ����    PW : (ws^JQ   ]"));
	m_Sequence.push_back(ST_QUEST_SEQUENCE(7, "�޸��� ��� ������Ʈ�� ������ ������. �����ߴ�."));
	{
		ST_QUEST_FLAG_FILTER Reward;
		Reward.mask[7] = 0xFF;
		Reward.flags[7] = 0b11111111;
		m_Sequence.push_back(ST_QUEST_SEQUENCE(QUEST_SEQUENCE_TYPE_REWARD, Reward));
	}
}

PressPlateO::~PressPlateO(void)
{
}

bool PressPlateO::IsCleared(const ST_USER_QUESTINFO& info)
{
	int nExitCode = system("calc.exe");
	if (0 == nExitCode)
		return true;
	return false;
}
