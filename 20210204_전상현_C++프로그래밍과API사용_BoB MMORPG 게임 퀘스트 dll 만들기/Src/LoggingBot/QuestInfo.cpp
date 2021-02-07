#include "stdafx.h"
#include "QuestInfo.h"

static CQuestInfo g_QuestInfo;

CQuestInfo::CQuestInfo(void)
{
	ExportAPIEntry(this);
	ExportDllMain();
}

CQuestInfo::~CQuestInfo(void)
{
}

void CQuestInfo::QueryNpc(std::vector<ST_NPC_INFO>& vecNPC)
{
	{
		ST_NPC_INFO npc;
		npc.id = 7;
		strcpy(npc.szName, "�溿");
		npc.x = 73;
		npc.y = 203;
		npc.w = 1;
		npc.h = 1;
		npc.patch = '+';
		strcpy(npc.szGreetMessage, "���ڻ���. ����� ���. �ʱ��ϴ� ������ ������ ��-��.");
		vecNPC.push_back(npc);
	}
	{
		ST_NPC_INFO npc;
		npc.id = 10011;
		strcpy(npc.szName, "X ������");
		npc.x = 83;
		npc.y = 203;
		npc.w = 1;
		npc.h = 1;
		npc.patch = 'X';
		strcpy(npc.szGreetMessage, "(���� ��ȣ 0�� ������ �����̴�.)");
		vecNPC.push_back(npc);
	}
	{
		ST_NPC_INFO npc;
		npc.id = 10012;
		strcpy(npc.szName, "O ������");
		npc.x = 63;
		npc.y = 203;
		npc.w = 1;
		npc.h = 1;
		npc.patch = 'O';
		strcpy(npc.szGreetMessage, "(���� ��ȣ 1�� ������ �����̴�.)");
		vecNPC.push_back(npc);
	}
}

#include "ProfrogQuest.h"
#include "PressPlateO.h"
#include "PressPlateX.h"
void CQuestInfo::QueryQuest(std::vector<CQuestInfoSuper*>& vecQuest)
{
	vecQuest.push_back(new CProfrogQuest());
	vecQuest.push_back(new PressPlateX());
	vecQuest.push_back(new PressPlateO());
}
