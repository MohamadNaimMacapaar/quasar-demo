<template>
  <div class="q-pa-md" style="background: #f7f9fb; min-height: 100vh">
    <!-- Top Category Buttons -->
    <div class="row q-col-gutter-md q-mb-lg">
      <div class="col">
        <q-btn
          class="full-width category-btn"
          :outline="selectedCategory !== 'cs'"
          :color="selectedCategory === 'cs' ? 'primary' : 'primary'"
          :text-color="selectedCategory === 'cs' ? 'white' : 'primary'"
          :class="selectedCategory === 'cs' ? 'category-active' : ''"
          @click="selectedCategory = 'cs'"
        >
          <span class="text-h6">Computer Science</span>
        </q-btn>
      </div>
      <div class="col">
        <q-btn
          class="full-width category-btn"
          :outline="selectedCategory !== 'it'"
          :color="selectedCategory === 'it' ? 'primary' : 'primary'"
          :text-color="selectedCategory === 'it' ? 'white' : 'primary'"
          :class="selectedCategory === 'it' ? 'category-active' : ''"
          @click="selectedCategory = 'it'"
        >
          <span class="text-h6">Information Technology</span>
        </q-btn>
      </div>
      <div class="col">
        <q-btn
          class="full-width category-btn"
          :outline="selectedCategory !== 'is'"
          :color="selectedCategory === 'is' ? 'primary' : 'primary'"
          :text-color="selectedCategory === 'is' ? 'white' : 'primary'"
          :class="selectedCategory === 'is' ? 'category-active' : ''"
          @click="selectedCategory = 'is'"
        >
          <span class="text-h6">Information Security</span>
        </q-btn>
      </div>
    </div>

    <!-- Section Title -->
    <div class="text-h6 text-bold q-mb-md" style="color: #2d3a4a">{{ categoryTitle }} Thesis</div>

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
          <div class="col-auto">
            <q-btn outline color="primary" label="View Details" />
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
    title: 'Test Bank System',
    approval: 'Approved',
    status: 'In Progress',
    color: '#ffe6ea',
  },
  {
    category: 'cs',
    title: 'Feeding Management System',
    approval: 'Pending',
    status: 'N/A',
    color: '#fff6e0',
  },
  {
    category: 'cs',
    title: 'UI payment Queuing System',
    approval: 'Rejected',
    status: 'N/A',
    color: '#ffe6ea',
  },
  {
    category: 'it',
    title: 'IT System',
    approval: 'Rejected',
    status: 'N/A',
    color: '#ffe6ea',
  },
  {
    category: 'is',
    title: 'IS System',
    approval: 'Rejected',
    status: 'N/A',
    color: '#ffe6ea',
  },
  // Add IT and IS theses here if needed
]

const categoryTitle = computed(() => {
  switch (selectedCategory.value) {
    case 'cs':
      return 'Computer Science'
    case 'it':
      return 'Information Technology'
    case 'is':
      return 'Information Security'
    default:
      return ''
  }
})

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
.category-btn {
  border-radius: 16px;
  font-weight: bold;
  transition:
    background 0.2s,
    color 0.2s;
}
.category-active {
  background: #1976d2 !important;
  color: #fff !important;
  box-shadow: 0 2px 8px #1976d233;
  border: 1.5px solid #1976d2 !important;
}
.thesis-card {
  border-radius: 16px;
  background: #fff;
}
</style>
