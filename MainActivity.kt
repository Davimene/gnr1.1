package com.example.geradordenumeroreal

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import com.example.geradordenumeroreal.databinding.MainActivityBinding

class MainActivity : ComponentActivity() {

    private lateinit var binding: MainActivityBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = MainActivityBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.iniciarApkBnt.setOnClickListener {
            val iniciar = Intent(this, PrimeiraTela::class.java)
            startActivity(iniciar)
        }

        binding.creditosBnt.setOnClickListener {
            val irCreditos = Intent(this, Creditos::class.java)
            startActivity(irCreditos)
        }

        binding.fecharApkBnt.setOnClickListener {
            finishAffinity()
        }
    }
}

