#include "stdafx.h"
#include "APIEntry.h"

static IQuestInfo* g_pQuestInfo;
void ExportAPIEntry(IQuestInfo* pIntance)
{
	g_pQuestInfo = pIntance;
}

DLL_API int QueryNpc(ST_NPC_INFO* outInfoArr)
{
	std::vector<ST_NPC_INFO> vecNPC;
	g_pQuestInfo->QueryNpc(vecNPC);

	if (vecNPC.empty())
		return 0;

	if (nullptr == outInfoArr)
		return vecNPC.size();

	memcpy(outInfoArr, &vecNPC[0], sizeof(ST_NPC_INFO) * vecNPC.size());
	return vecNPC.size();
}

DLL_API int QueryQuest(CQuestInfoSuper** outInfoArr)
{
	std::vector<CQuestInfoSuper*> vecQuest;
	g_pQuestInfo->QueryQuest(vecQuest);

	if (vecQuest.empty())
		return 0;

	if (nullptr == outInfoArr)
		return vecQuest.size();

	memcpy(outInfoArr, &vecQuest[0], sizeof(CQuestInfoSuper*) * vecQuest.size());
	return vecQuest.size();
}
