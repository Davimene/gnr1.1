package com.example.geradordenumeroreal

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.geradordenumeroreal.databinding.ActivityNumerosSalvosBinding

class NumerosSalvos : AppCompatActivity() {
    private lateinit var binding: ActivityNumerosSalvosBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityNumerosSalvosBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.voltarBnt.setOnClickListener {

            val voltar = Intent(this, PrimeiraTela::class.java)
            startActivity(voltar)
        }

    }
}
