<template>
  <div class="q-pa-md" style="background: #f7f9fb; min-height: 100vh">
    <!-- Top Category Buttons -->
    <div class="row q-col-gutter-md q-mb-lg">
      <div class="col">
        <q-btn
          class="full-width"
          color="white"
          text-color="primary"
          unelevated
          :class="selectedCategory === 'cs' ? 'category-active' : ''"
          @click="selectedCategory = 'cs'"
        >
          <span class="text-h6">Computer Science</span>
        </q-btn>
      </div>
      <div class="col">
        <q-btn
          class="full-width"
          color="white"
          text-color="primary"
          unelevated
          :class="selectedCategory === 'it' ? 'category-active' : ''"
          @click="selectedCategory = 'it'"
        >
          <span class="text-h6">Information Technology</span>
        </q-btn>
      </div>
      <div class="col">
        <q-btn
          class="full-width"
          color="white"
          text-color="primary"
          unelevated
          :class="selectedCategory === 'is' ? 'category-active' : ''"
          @click="selectedCategory = 'is'"
        >
          <span class="text-h6">Information Security</span>
        </q-btn>
      </div>
    </div>

    <!-- Section Title -->
    <div class="text-h6 text-bold q-mb-md" style="color: #2d3a4a">Recent Thesis</div>

    <!-- Thesis Cards -->
    <div>
      <q-card v-for="(thesis, idx) in filteredTheses" :key="idx" class="q-mb-md thesis-card" flat>
        <div class="row items-center q-pa-md">
          <div class="col-auto">
            <div
              class="q-mr-md"
              :style="`width:40px;height:40px;border-radius:12px;background:${thesis.color};`"
            ></div>
          </div>
          <div class="col">
            <div class="text-subtitle1 text-weight-medium">{{ thesis.title }}</div>
            <div class="row q-mt-xs">
              <div class="col-auto q-mr-lg">
                <span class="text-caption">Approval</span><br />
                <span :class="approvalClass(thesis.approval)">{{ thesis.approval }}</span>
              </div>
              <div class="col-auto">
                <span class="text-caption">Status</span><br />
                <span :class="statusClass(thesis.status)">{{ thesis.status }}</span>
              </div>
            </div>
          </div>
          <div class="col-auto q-gutter-sm">
            <q-btn outline color="primary" label="Edit Details" size="sm" />
            <q-btn outline color="primary" label="Hide" size="sm" />
            <q-btn outline color="primary" label="Remove" size="sm" />
          </div>
        </div>
      </q-card>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedCategory = ref('cs')

const theses = [
  {
    category: 'cs',
    title: 'Lending Management system',
    approval: 'Pending',
    status: 'N/A',
    color: '#fff6e0',
  },
  {
    category: 'cs',
    title: 'Online Scoring System',
    approval: 'Pending',
    status: 'N/A',
    color: '#fff6e0',
  },
  // Add more theses for IT and IS as needed
]

const filteredTheses = computed(() => theses.filter((t) => t.category === selectedCategory.value))

function approvalClass(status) {
  if (status === 'Approved') return 'text-primary'
  if (status === 'Pending') return 'text-warning'
  if (status === 'Rejected') return 'text-negative'
  return ''
}

function statusClass(status) {
  if (status === 'In Progress') return 'text-primary'
  return 'text-grey'
}
</script>

<style scoped>
.category-active {
  background: #e6edfa !important;
  color: #222 !important;
  font-weight: bold;
  border-radius: 16px;
}
.thesis-card {
  border-radius: 16px;
  background: #fff;
}
</style>
